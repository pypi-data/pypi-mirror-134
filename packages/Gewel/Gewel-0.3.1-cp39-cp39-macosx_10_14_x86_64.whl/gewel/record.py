"""
This module contains
code related to record scenes for use outside gewel.
For example, it contains the class :py:class:`~Mp4Recorder`
which is used to record scenes to .mp4 files.
"""


import os
from abc import ABC, ABCMeta, abstractmethod
from time import perf_counter
from typing import IO, Optional, Union

import cairocffi as cairo
import cv2
import imageio
import numpy as np

from gewel.draw import Drawable, TransformedDrawable, Scene


class Recorder(ABC):

    def __init__(self):
        self._recording_time = 0.0
        self._frames_recorded = 0

    def reset_metrics(self):
        self._recording_time = 0.0
        self._frames_recorded = 0

    @property
    def recording_time(self) -> float:
        return self._recording_time

    @property
    def frames_recorded(self) -> int:
        return self._frames_recorded

    @abstractmethod
    def record_frame(self, frame: int, surface: cairo.ImageSurface):
        raise NotImplementedError('Recorder.record_frame is abstract.')

    def start_recording(self, fps: float, width: int, height: int):
        pass

    def end_recording(self):
        pass

    def record(
            self,
            scene: Scene,
            duration: Optional[float] = None,
            t0: float = 0.0,
            fps: float = 30.0,
            width: Optional[int] = None,
            height: Optional[int] = None,
    ):
        if duration is None:
            duration = scene.time

        if width is None:
            width = scene.render_width or 640

        if height is None:
            height = scene.render_height or 480

        self.start_recording(fps, width, height)

        frame, frame_time = 0, t0
        end_time = t0 + duration

        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
        ctx = cairo.Context(surface)

        while frame_time <= end_time:
            with ctx:
                scene.draw(ctx, frame_time)

                frame_recording_start = perf_counter()
                self.record_frame(frame, surface)
                frame_recording_end = perf_counter()
                frame_recording_time = frame_recording_end - frame_recording_start

                frame += 1
                frame_time = t0 + frame / fps

                self._frames_recorded += 1
                self._recording_time += frame_recording_time

        self.end_recording()


class FrameFileRecorder(Recorder):
    def __init__(self, dir_path: str, filename='frame'):
        super().__init__()
        self._dir_path: str = dir_path
        self._filename: str = filename

    def record_frame(self, frame: int, surface: cairo.ImageSurface):
        filename = '{:}_{:06d}.png'.format(self._filename, frame)
        filepath = os.path.join(self._dir_path, filename)
        surface.write_to_png(filepath)


class FileRecorder(Recorder, metaclass=ABCMeta):
    def __init__(self, file_path: Union[str, IO], extension: str):
        super().__init__()

        if isinstance(file_path, str):
            self._file_path = file_path if file_path.endswith(extension) else file_path + extension
        else:
            self._file_path = file_path

        self._height = 0
        self._width = 0


class Mp4Recorder(FileRecorder):
    def __init__(self, file_path: Union[str, IO]):
        super().__init__(file_path, '.mp4')
        self._writer = None

    def start_recording(self, fps: float, width: int, height: int):
        super().start_recording(fps, width, height)

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self._writer = cv2.VideoWriter(self._file_path, fourcc, fps, (width, height))

        self._height = height
        self._width = width

    def end_recording(self):
        self._writer.release()
        self._writer = None
        self._height = 0
        self._width = 0

        super().end_recording()

    def record_frame(self, frame: int, surface: cairo.ImageSurface):
        surface.flush()
        buf = surface.get_data()

        rgba_data = np.ndarray(shape=(self._height, self._width, 4), dtype=np.uint8, buffer=buf)
        self._writer.write(rgba_data[:, :, :3])


class GifRecorder(FileRecorder):
    def __init__(self, file_path: Union[str, IO]):
        super().__init__(file_path, '.gif')
        self._writer = None

    def start_recording(self, fps: float, width: int, height: int):
        super().start_recording(fps, width, height)
        self._writer = imageio.get_writer(self._file_path, mode='I', fps=fps)

        self._height = height
        self._width = width

    def record_frame(self, frame: int, surface: cairo.ImageSurface):
        surface.flush()
        buf = surface.get_data()

        rgba_data = np.ndarray(shape=(self._height, self._width, 4), dtype=np.uint8, buffer=buf)
        r_data, g_data, b_data = rgba_data[:, :, 0], rgba_data[:, :, 1], rgba_data[:, :, 2]
        data = np.stack([b_data, g_data, r_data], axis=2)

        self._writer.append_data(data)

    def end_recording(self):
        self._writer.close()

        self._writer = None
        self._height = 0
        self._width = 0

        super().end_recording()


def scale_to_fit_xform(
        from_width: float, from_height: float,
        to_width: float, to_height: float
) -> cairo.Matrix:
    from_aspect = from_width / from_height
    to_aspect = to_width / to_height

    if from_aspect > to_aspect:
        # Originally wider, so scale by width.
        scale = to_width / from_width
    else:
        # Originally taller, so scale by height.
        scale = to_height / from_height

    shift_0 = cairo.Matrix(x0=-0.5 * from_width, y0=-0.5 * from_height)
    scale = cairo.Matrix(xx=scale, yy=scale)
    shift_1 = cairo.Matrix(x0=0.5 * to_width, y0=0.5 * to_height)

    xf = shift_0 * scale * shift_1
    return xf


def scale_to_fit(
        drawable: Drawable,
        from_width: float, from_height: float,
        to_width: float, to_height: float
) -> Drawable:
    xf = scale_to_fit_xform(from_width, from_height, to_width, to_height)
    return TransformedDrawable(
        drawable,
        xx=xf.xx, yx=xf.yx, xy=xf.xy, yy=xf.yy, x0=xf.x0, y0=xf.y0,
        z=drawable.z
    )


RESOLUTION_4K = 3840, 2160
RESOLUTION_8K = 7680, 4320
RESOLUTION_1080P = 1920, 1080
RESOLUTION_720P = 1280, 720
RESOLUTION_VGA = 640, 480
RESOLUTION_VGA_16_9 = 640, 360
