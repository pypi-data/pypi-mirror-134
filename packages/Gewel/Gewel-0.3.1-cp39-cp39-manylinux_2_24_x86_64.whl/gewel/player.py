"""
This module contains
the class :py:class:`gewel.player.Player` that
implements an interactive player for scenes constructed
using gewel.
"""

import collections
import os.path
import queue
import threading
import tkinter
from time import perf_counter
from tkinter import filedialog, ttk, Tk, E, W, HORIZONTAL, LEFT, CENTER, RIGHT
from typing import Optional

import cairocffi as cairo
from PIL import Image, ImageTk

import gewel.record
import tvx
import tvx.utils
from gewel.draw import Scene


class RenderThread(threading.Thread):

    def __init__(self, target: 'Player', daemon: bool = False):
        super().__init__(daemon=daemon)
        self._target = target

    def run(self):
        while self._target.running:
            time = self._target.render_time_queue_get()
            self._target.render_image(time)


class Player(Tk):

    _slider_width = 0.1

    @classmethod
    def load_image(cls, filename: str) -> Optional[tkinter.Image]:
        path = os.path.join(
            os.path.dirname(__file__),
            "images",
            filename)
        try:
            image = tkinter.PhotoImage(file=path)
        except tkinter.TclError:
            image = None

        return image

    def __init__(
            self, scene: Scene,
            width: int = 640,
            height: int = 480,
            start: float = 0.0,
            duration: Optional[float] = None,
            autoplay: bool = True,
            loop: bool = True,
    ):
        super().__init__()
        self._scene = scene
        self._render_width = width
        self._render_height = height
        self._start = start
        if duration is None:
            duration = scene.time
        self._duration = duration
        self._loop = loop
        self._time = start
        self._running = True

        # We only ever need one pending render time. If there is
        # alpha new one while the rendering thread is rendering, we'll
        # just replace it.
        self._render_time_queue: queue.Queue = queue.Queue(1)

        # The queue that images come back on.
        # Again there is no point in having
        # more than one because the latest one
        # is the one we are going to want to draw.
        self._image_queue: queue.Queue = queue.Queue(1)

        # Cairo rendering.
        self._surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
        self._ctx = cairo.Context(self._surface)

        def _xview(cmd, a, b=None):
            if cmd == 'moveto':
                pos = float(a)
                time = self._scroll_pos_to_time(pos)
                self._queue_up_rendering_time(time)
            elif cmd == 'scroll' and b == 'pages':
                delta_t = 10.0 * float(a)
                time = max(self._start, min(self._start + self._duration, self._time + delta_t))
                self._queue_up_rendering_time(time)

        self.xview = _xview

        self._scrollbar = ttk.Scrollbar(self, orient=HORIZONTAL, command=self.xview)
        self.yscrollcommand = self._scrollbar.set

        bottom_row = ttk.Frame(self)

        self._time_label = ttk.Label(bottom_row, text="00:00.000", width=12, anchor=CENTER)
        self._fps_label = ttk.Label(bottom_row, text="", width=12, anchor=CENTER)

        self._image_label = ttk.Label(self)

        def _update_image_handler() -> None:
            """
            This should happen on the main thread in response
            to a message that it is time to maybe update the
            image if there is anything in the queue.

            Returns
            -------
                None
            """

            # Drain the queue. No point in doing anything
            # with images that are old.
            time, rendered_image = None, None

            while True:
                try:
                    time, rendered_image = self._image_queue.get(block=False)
                except queue.Empty:
                    break

            # If there was at least one image in the queue, we
            # should have the last image in the queue before it
            # became empty.
            if rendered_image is not None:
                if self._image_label is None:
                    self._image_label = ttk.Label(self, image=rendered_image)
                else:
                    self._image_label.configure(image=rendered_image)
                    self._image_label.image = rendered_image

                # Move the scrollbar to the time we just displayed an image for.
                self._update_ui_to_time(time)

            # This upper bounds us at 200fps, but that's
            # probably fine.
            self.after(5, _update_image_handler)

        _update_image_handler()

        self._playing = False
        self._play_start_time = 0.0
        self._render_start_real_time = 0.0

        # self.render_image(self._time)

        self._frame_times = collections.deque(maxlen=10)

        self._update_ui_to_time(self._time)

        def _play_pause(play=None):
            if play is not None:
                self._playing = play
            else:
                self._playing = not self._playing
            self._config_play_pause_button()
            if self._playing:
                # Kick us off by rendering 1/60th of a second
                # from now and then we will continuously render
                # from there.
                self._play_start_time = self._time + 1.0 / 60
                self._render_start_real_time = perf_counter()
                self._queue_up_rendering_time(self._play_start_time)
            else:
                self._update_ui_to_time(self._time)

        def _pause():
            _play_pause(play=False)
            # And drain the queues.
            try:
                self._render_time_queue.get(block=False)
            except queue.Empty:
                pass
            try:
                self._image_queue.get(block=False)
            except queue.Empty:
                pass

        self._pause_func = _pause

        def _loop_command():
            self._loop = self._loop_var.get() != 0

        self._play_icon = self.load_image('play.png')
        self._pause_icon = self.load_image('pause.png')

        self._play_button = ttk.Button(
            bottom_row,
            text='Play', image=self._play_icon,
            width=7,
            command=_play_pause
        )

        self._loop_var = tkinter.IntVar(bottom_row, 1 if self._loop else 0)

        self._loop_button = ttk.Checkbutton(
            bottom_row,
            text='Loop',
            width=7,
            variable=self._loop_var,
            command=_loop_command
        )

        self._image_label.grid(row=0, column=0)
        self._scrollbar.grid(row=1, column=0, sticky=(E, W))

        bottom_row.grid(row=2, column=0, sticky=(E, W))
        self._time_label.pack(side=LEFT)
        self._fps_label.pack(side=LEFT)
        self._play_button.pack(side=LEFT)
        self._loop_button.pack(side=RIGHT)

        for ii in range(5):
            self.columnconfigure(ii, weight=1)

        self.winfo_toplevel().title("Player")

        # Start the rendering thread.
        self._render_thread = RenderThread(self, daemon=True)
        self._render_thread.start()

        self._queue_up_rendering_time(self._time)

        menu_bar = tkinter.Menu(self)

        file_menu = tkinter.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Save .mp4", command=lambda: self.save_as('.mp4'))
        file_menu.add_command(label="Save .gif", command=lambda: self.save_as('.gif'))
        file_menu.add_separator()
        file_menu.add_command(label='Quit', command=self.destroy)

        menu_bar.add_cascade(label="File", menu=file_menu)

        self.config(menu=menu_bar)

        if autoplay:
            # Give us a second for the UI to settle down
            # and then start playing.
            self.after(1000, _play_pause, True)

    def _image_from_surface(self) -> ImageTk.PhotoImage:
        return ImageTk.PhotoImage(
            Image.frombuffer(
                "RGBA", (self._render_width, self._render_height),
                self._surface.get_data(), "raw", "BGRA", 0, 1
            )
        )

    @property
    def running(self) -> bool:
        return self._running

    def _config_play_pause_button(self):
        icon, text = (self._pause_icon, 'Pause') if self._playing else (self._play_icon, 'Play')

        self._play_button.configure(text=text)
        self._play_button.configure(image=icon)
        self._play_button.image = icon

    def _time_to_scroll_pos(self, time) -> float:
        fractional_time = (time - self._start) / self._duration
        pos = fractional_time * (1 - self._slider_width)
        return pos

    def _scroll_pos_to_time(self, pos) -> float:
        fractional_time = pos / (1 - self._slider_width)
        time = self._start + fractional_time * self._duration
        time = max(self._start, min(self._start + self._duration, time))
        return time

    def render_time_queue_get(self, block: bool = True, timeout: Optional[float] = None):
        return self._render_time_queue.get(block=block, timeout=timeout)

    def destroy(self):
        # Tell the render thread it can exit from its loop.
        self._running = False
        super().destroy()

    def _queue_up_rendering_time(self, time: float):
        # Pull whatever might be on the queue off.
        # We don't have to render those since the
        # current request is newer and will overwrite
        # them.
        time = min(time, self._start + self._duration)

        while True:
            try:
                self._render_time_queue.get(block=False)
            except queue.Empty:
                pass

            try:
                self._render_time_queue.put(time)
                break
            except queue.Full:
                pass

    def render_image(self, time: float) -> None:
        """
        This is meant to be called from a :py:class:`~RenderThread`,
        since it may take a non-trivial amount of time to render a
        scene. When it finishes, it puts the image it rendered onto
        a queue for the main Tk thread to put into the view.

        Parameters
        ----------
        time
            The scene time to render.

        Returns
        -------
        None
        """
        # Render the frame.
        self._scene.draw(self._ctx, time)

        rendered_image = self._image_from_surface()
        self._image_queue.put((time, rendered_image))

        self._time = time

        if self._playing:
            # Queue up another frame.
            frame_done_time = perf_counter()
            frame_elapsed_time = frame_done_time - self._render_start_real_time
            self._frame_times.append(frame_elapsed_time)
            self._render_start_real_time = perf_counter()
            next_frame_time = min(self._time + frame_elapsed_time, self._start + self._duration)
            if next_frame_time >= self._start + self._duration:
                next_frame_time = self._start
                if not self._loop:
                    self._playing = False
                    self._config_play_pause_button()
            self._queue_up_rendering_time(next_frame_time)

    def _update_ui_to_time(self, time) -> None:
        """
        Set the scroll bar based on the current time and
        geometry of the image and update the time label.

        Returns
        -------
        None
        """
        pos = self._time_to_scroll_pos(time)
        start, end = pos, pos + self._slider_width
        self.yscrollcommand(start, end)

        time_string = tvx.utils.format_time(time, False)
        self._time_label.configure(text=time_string)

        if self._playing and len(self._frame_times) > 0:
            fps = len(self._frame_times) / sum(self._frame_times)
            fps_string = "{:.1f} fps".format(fps)
            self._fps_label.configure(text=fps_string)
        else:
            self._fps_label.configure(text='')

    def save_as(self, extension: str):
        def _save_dialog():
            f = filedialog.SaveAs(defaultextension=extension).show()
            if f is not None:
                if extension == '.gif':
                    recorder = gewel.record.GifRecorder(f)
                elif extension == '.mp4':
                    recorder = gewel.record.Mp4Recorder(f)
                else:
                    # Default to mp4.
                    recorder = gewel.record.Mp4Recorder(f)

                recorder.record(self._scene, t0=self._start, duration=self._duration)

        pause = self._pause_func
        pause()
        self.after(200, _save_dialog)
