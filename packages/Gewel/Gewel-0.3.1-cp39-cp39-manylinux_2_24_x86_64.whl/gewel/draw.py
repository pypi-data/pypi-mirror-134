"""
This module contains classes and functions for drawing.

:ref:`gewel_getting_started` is an introduction to gewel
that is useful if you are just getting started.

:ref:`code_samples` contains numerous examples of the use of
classes from this module to create simple animations.
"""

import bisect
import re
from abc import ABCMeta, abstractmethod
from contextlib import contextmanager
from dataclasses import dataclass
from enum import Enum
from io import BytesIO
from time import perf_counter
from typing import IO, Iterable, List, Optional, Protocol, Tuple, Union

import IPython.display
import cairocffi as cairo
import ipywidgets as widgets
import numpy as np

import gewel.color
import tvx
import tvx.utils
from gewel._timekeeper import TimekeeperProtocol, TimekeeperMixin
from gewel.color import BaseColor, ColorMap, TRANSPARENT, BACKGROUND, BLACK
from tvx import float_at_time

_total_device_drawing_time = 0.0


def reset_total_device_drawing_time():
    """
    Reset the total device rendering time. See
    :py:func:`~total_device_drawing_time` for more
    details.

    Returns
    -------

    """
    global _total_device_drawing_time
    _total_device_drawing_time = 0.0


def total_device_drawing_time() -> float:
    """
    Get the total time spent in rendering at the low
    level. Normally used only for performance debugging.
    This value begins at 0.0 before any rendering is done
    and can be reset by calling
    :py:func:`~reset_total_device_drawing_time`.

    Returns
    -------
    float
        Total device rendering time.
    """
    return _total_device_drawing_time


@contextmanager
def _time_device_drawing():
    global _total_device_drawing_time

    start = perf_counter()
    try:
        yield
    finally:
        end = perf_counter()
        _total_device_drawing_time += end - start


@contextmanager
def _xform_context(ctx: cairo.Context, xform: cairo.Matrix):
    try:
        ctx.save()
        ctx.transform(xform)
        yield ctx
    finally:
        ctx.restore()


@contextmanager
def _clipped_rectangle_context(ctx: cairo.Context, x0, y0, x1, y1):
    try:
        ctx.save()
        ctx.move_to(x0, y0)
        ctx.line_to(x0, y1)
        ctx.line_to(x1, y1)
        ctx.line_to(x1, y0)
        ctx.close_path()
        ctx.clip()
        yield ctx
    finally:
        ctx.restore()


_radians_per_degree = np.pi / 180.0


@dataclass(init=False)
class Drawable(TimekeeperMixin, metaclass=ABCMeta):
    """
    This is the abstract base class for all drawables.

    Drawables typically have two distinct phases in their lifecycle,
    `scripting` and `rendering`. Scripting sets up the object
    and all the actions it will take during a scene. It is like writing
    the script for the animation. Rendering animates the scene, producing
    a final video of the scene. It is like filming a scene after
    the script has been written.

    For more details on the lifecycle of a :py:class:`~Drawable`, please refer to
    :ref:`draw_lifecycle`.

    Parameters
    ----------
    z
        Depth of the object. When a :py:class:`~Scene` is rendered, the
        :py:class:`~Drawable` objects in the scene are rendered in ascending `z`
        order. So if two objects in the scene overlap, the one with the
        larger z will appear to be on top when the scene is rendered. If the
        z value are equal, the rendering order is undefined. So if there
        are two objects that are likely to overlap, it is recommended they
        be given different `z` values to ensure consistent rendering.
    alpha
        The transparency/opacity of the object. It should be in the range
        [0.0, 1.0]. 0.0 means fully transparent, so when the drawn nothing
        appears. 1.0 is fully opaque, so nothing drawn at a lower `z` will
        show through. If in between 0.0 and 1.0, the object is partially
        transparent so objects with lower `z` will be partially visible through
        it. The closer to 0.0 the value is, the more transparent it will be.

        Note that :py:class:`~gewel.color.Color` objects have their own
        alpha attribute. So if the color of a drawable is set to a transparent
        or semi-transparent color, then other objects may show through it even
        if the alpha of the object itself is set to 1.0.
    """
    z: tvx.FloatOrTVF = 0.0  #: `z` depth of the object. Objects in a scene are rendered
    # in order from lowest `z` depth to highest.

    alpha: tvx.FloatOrTVF = 1.0  #: Transparency/opacity. A value of 0.0 means completely
    # transparent. A value of 1.0 means completely opaque. Anything
    # in-between means partially transparent, with values closer
    # to zero being more transparent.

    def __init__(self, z: tvx.FloatOrTVF = 0.0, alpha: tvx.FloatOrTVF = 1.0):
        self.z = z
        self.alpha = alpha
        self._time = 0.0

    @property
    def time(self) -> float:
        """
        The next-action time. See :ref:`draw_update_time` for more on next-action time.

        Returns
        -------
        float
            The next action time.
        """
        return self._time

    def set_time(self, t: float):
        """
        Set the next-action time.

        See :ref:`draw_update_time` for more on next-action time.

        Parameters
        ----------
        t
            The new next-action time.
        """
        self._time = t

    @abstractmethod
    def draw(self, ctx: cairo.Context, t: float) -> None:
        """
        This method renders the drawable into pixels. :py:class:`~Drawable` objects
        typically have time-varying behavior. For example, the `x` and `y` location
        of the object in a scene may be time-varying floats (see the :py:class:`~tvx.Tvf`
        class for details). It is the responsibility of the :py:meth:`~draw` method
        to render the correct pixels for time passed in.

        Note that this method is very rarely called directly by user code. Instead,
        it is called by utility classes that render a :py:class:`~Scene` containing
        a :py:class:`~Drawable` objects. Examples include
        :py:class:`gewel.record.Mp4Recorder`, which renders a scene to an MP4
        file, or :py:class:`gewel.player.Player` that creates an interactive
        preview of a :py:class:`~Scene` or the :py:meth:`gewel.draw.Scene.__repr__`
        method that render a scene into an IPython notebook widget.

        Parameters
        ----------
        ctx
            The context in which to render. This is an object with low-level
            drawing primitives that the :py:meth:`~draw` method relies on to
            render at the pixel level.
        t
            The time at which to render. That is, we should render the object
            as it is intended to appear at this time in the scene. Exactly what
            that is is typically controlled by properties of the object that
            are :py:class:`~tvx.Tvf` objects.
        """
        pass

    def fade_to(self, alpha: tvx.FloatOrTVF, duration: float, update_time: bool = True):
        """
        Fade the object from it's current alpha to a new value. Alpha values range
        from 0.0, which means completely transparent, to 1.0, which means completely opaque. Most
        newly constructed :py:class:`~Drawable` classes that support alpha default to a value of 1.0.

        See :ref:`fade_to_sample` for sample usage.

        Parameters
        ----------
        alpha
            The new alpha value. Should be between 0.0 and 1.0, inclusive.
            Values outside this range produce undefined behavior that may
            change in future versions.
        duration
            The amount of time, in seconds, the fade from the current
            alpha to the new alpha should take.
        update_time
            Should the object's time be updated. Normally this is `True`. Making
            it `False` does not change the time, so that other updates can be
            made on the same object at the same time it is fading. For example, :py:meth:`~move_to`
            can be called to make the object move as it fades.

        Returns
        -------
        None
        """
        self.alpha = tvx.ramp(self.alpha, alpha, self.time, width=duration)
        self._manage_time(duration, update_time)

    def __getitem__(self, item: Union[float, slice]) -> 'ClipDrawable':
        """
        Get the frame at a specific time or a clip
        covering a range from start to end time.

        Parameters
        ----------
        time
            Either a float, in which case the return value is a
            frame at the given time, or a slice of the form ``start:end``,
            in which case the return value is a clip of the scene covering
            that range of time.
        Returns
        -------
        ClipDrawable
            A frame or a clip, depending on whether the argument was
            a float or a slice.
        """
        if isinstance(item, slice):
            return ClipDrawable(self, item.start, item.stop)
        else:
            raise IndexError("Only two-element slice indices, are supported. Try d[start:stop].")

    def transformed(
            self,
            xx: tvx.FloatOrTVF = 1.0,
            yx: tvx.FloatOrTVF = 0.0,
            xy: tvx.FloatOrTVF = 0.0,
            yy: tvx.FloatOrTVF = 1.0,
            x0: tvx.FloatOrTVF = 0.0,
            y0: tvx.FloatOrTVF = 0.0,
            z: Optional[tvx.FloatOrTVF] = None
    ) -> 'Drawable':
        """
        Construct and return a new drawable that is transformed by
        the translation matrix specified by the parameters. The
        default parameter values produce the identity transform.

        The location of any point (`x`, `y`) in the original
        drawable is translated to the new point (`x`\', `y`\')
        where

            `x`\' = ``xx`` * `x` + ``xy`` * `y` + ``x0``

        and

            `y`\' = ``yy`` * `y` + ``yx`` * `x` + ``y0``

        Parameters
        ----------
        xx
            Element of the matrix.
        yx
            Element of the matrix.
        xy
            Element of the matrix.
        yy
            Element of the matrix.
        x0
            Translation in `x`
        y0
            Translation in `y`
        z
            z depth of the new drawable. If ``None`` then ``self.z`` is used.

        Returns
        -------
        Drawable
            A transformed version of ``self``.
        """
        if z is None:
            z = self.z
        return TransformedDrawable(self, xx=xx, yx=yx, xy=xy, yy=yy, x0=x0, y0=y0, z=z)

    def translated(self, dx: tvx.FloatOrTVF, dy: tvx.FloatOrTVF, z: Optional[tvx.FloatOrTVF] = None) -> 'Drawable':
        """
        Construct and return a new drawable that is translated by a relative amount
        in the x and y directions.

        Parameters
        ----------
        dx
            How far to translate in the `x` direction.
        dy
            How far to translate in the `y` direction.
        z
            The z depth of the resulting drawable. If not
            supplied, the z depth of ``self`` is used.

        Returns
        -------
        Drawable
            A new drawable that renders as the original but translated.
        """
        if z is None:
            z = self.z
        return TransformedDrawable(self, x0=dx, y0=dy, z=z)

    def scaled(
            self,
            sx: tvx.FloatOrTVF,
            sy: Optional[tvx.FloatOrTVF] = None,
            z: Optional[tvx.FloatOrTVF] = None
    ) -> 'Drawable':
        """
        Construct and return a new drawable that is scaled
        in the x and y directions.

        Parameters
        ----------
        sx
            Scale in the `x` direction.
        sy
            Scale in the `y` direction.
        z
            The z depth of the resulting drawable. If not
            supplied, the z depth of ``self`` is used.

        Returns
        -------
        Drawable
            A new drawable that renders as the original but scaled.
        """
        if sy is None:
            sy = sx
        if z is None:
            z = self.z
        return TransformedDrawable(self, xx=sx, yy=sy, z=z)

    def rotated(self, radians: tvx.FloatOrTVF, z: Optional[tvx.FloatOrTVF] = None) -> 'Drawable':
        """
        Return a version of the drawable that is rotated. See also
        :py:meth:`~Drawable.rotated_degrees`.

        Parameters
        ----------
        radians
            How much to rotate by, in radians.
        z
            The z depth of the resulting drawable. If not
            supplied, the z depth of ``self`` is used.

        Returns
        -------
        Drawable
            A new drawable that renders as the original but rotated.
        """
        if z is None:
            z = self.z
        return RotatedDrawable(self, radians=radians, z=z)

    def rotated_degrees(self, degrees: tvx.FloatOrTVF, z: Optional[tvx.FloatOrTVF] = None) -> 'Drawable':
        """
        Return a version of the drawable that is rotated. See also
        :py:meth:`~Drawable.rotated`.

        Parameters
        ----------
        degrees
            How much to rotate by, in degrees.
        z
            The z depth of the resulting drawable. If not
            supplied, the z depth of ``self`` is used.

        Returns
        -------
        Drawable
            A new drawable that renders as the original but rotated.
        """
        if z is None:
            z = self.z
        return RotatedDrawable(self, radians=degrees * _radians_per_degree, z=z)


class TimeWindowDrawable(Drawable):
    """
    A wrapper class that makes a drawable visible only in a certain time
    range.

    Note that this class is rarely one you will want to use directly. More often
    you will want to use the method :py:meth:`~Drawable.fade_to` in order to produce
    an animation in which an objects appears and or disappears at various times. This
    class is used internally inside methods like :py:meth:`~XYDrawable.move_to`.

    This wrapper class takes a :py:class:`~Drawable` `d` at construction time,
    draws itself exactly as `d` would between times `t0` and `t1`, but is completely
    invisible at any time before `t0` or after `t1`.

    Parameters
    ----------
    d
        A drawable that we only want to appear during a single specific time range.
    t0
        The beginning of the time range when `d` should appear. It will not be
        visible before this time.
    t1
        The end of the time range when `d` should appear. It will not be visible
        after this time.
    z
        The z-order of the drawable.
    """
    def __init__(self, d: Drawable, t0: float, t1: float, z: tvx.FloatOrTVF = 0.0):
        super().__init__(z=z)
        self._d = d
        self._t0 = t0
        self._t1 = t1

    def draw(self, ctx: cairo.Context, t: float) -> None:
        if self._t0 <= t < self._t1:
            self._d.draw(ctx, t)


@dataclass(init=False)
class XYDrawable(Drawable, metaclass=ABCMeta):
    """
    An abstract base class for :py:class:`~Drawable`
    objects that that have a specific location
    specified by a point (`x`, `y`) and a rotation
    specified by an angle `theta`. Most commonly used
    drawable classes derive from this class.

    Parameters
    ----------
    x
        x location
    y
        y location
    theta
        Angle of rotation
    z
        z depth
    alpha
        opacity. 0.0 = transparent; 1.0 = opaque
    """

    x: tvx.FloatOrTVF = 0.0  #: `x` value of the object's location. May be time-varying.
    y: tvx.FloatOrTVF = 0.0  #: `y` value of the object's location. May be time-varying.
    theta: tvx.FloatOrTVF = 0.0  #: Angle of rotation in radians. May be time-varying.

    def __init__(
            self,
            x: tvx.FloatOrTVF = 0.0,
            y: tvx.FloatOrTVF = 0.0,
            theta: tvx.FloatOrTVF = 0.0,
            z: tvx.FloatOrTVF = 0.0,
            alpha: tvx.FloatOrTVF = 1.0,
    ):
        super().__init__(z=z, alpha=alpha)
        self.x = x
        self.y = y
        self.theta = theta

    def xy(self) -> Tuple[tvx.FloatOrTVF, tvx.FloatOrTVF]:
        """
        Return the possibly time-varying values of `x` and `y`.

        Returns
        -------
        Tuple[tvx.FloatOrTVF, tvx.FloatOrTVF]
            The tuple ``(self.x, self.y)``.
        """
        return self.x, self.y

    _SCAFFOLD_PATH_COLOR = gewel.color.Color(0.5, 0.5, 0.5, 0.5)
    _SCAFFOLD_POINT_COLOR = gewel.color.Color(0.25, 0.25, 1.0, 0.5)
    _SCAFFOLD_OBJECT_COLOR = gewel.color.Color(1.0, 0.25, 0.25, 0.5)

    def move_to(
            self,
            x: float, y: float, duration: float,
            update_time: bool = True,
            scaffold: bool = False
    ) -> Optional[Drawable]:
        """
        Move to a new location over the course of a given amount of time.
        This method is used in the scripting phase of the object's lifetime
        to schedule it to move from one location on or off-screen to another.
        This is one of the core methods used to produce animations.

        The object follows a linear path parameterized by :math:`t` which
        varies from 0 to 1 over the duration of motion. The position of
        the object for any given value of :math:`t` is

        .. math::

              x = (1 - t) x_0 + t x_1

              y = (1 - t) y_0 + t y_1

        Note that when :math:`t = 0`, :math:`x = x_0` and :math:`y = y_0`, putting us
        at the starting point. When :math:`t = 1`, :math:`x = x_1` and :math:`y = y_1`, putting us
        at the final point.

        See :ref:`move_to_sample` for sample usage.

        Parameters
        ----------
        x
            The x coordinate to move to.
        y
            The y coordinate to move to.
        duration
            The amount of time, in seconds, the move from the current
            location to the new location should take.
        update_time
            Should the object's time be updated. Normally this is `True`. Making
            it `False` does not change the time, so that other updates can be
            made on the same object at the same time it is moving. For example, :py:meth:`~rotate_to`
            can be called to make the object spin as it moves.
        scaffold
            Should we also generate scaffolding to show the path that the object
            will move along during animation? This is primarily for debugging purposes.
        Returns
        -------
        :py:class:`~Drawable` or ``None``
            ``None`` if ``scaffold`` is ``False`` or a :py:class:`~Drawable` representing
            the scaffolding if the ``scaffold`` is ``True``.
        """
        x0, y0 = self.x, self.y
        xt, yt = tvx.utils.path(x0, y0, x, y, start=self.time, duration=duration)
        self.x = tvx.cut(self.x, self.time, xt)
        self.y = tvx.cut(self.y, self.time, yt)

        if scaffold:
            path = PathDrawable([x0, x], [y0, y], color=XYDrawable._SCAFFOLD_PATH_COLOR)
            start_marker = MarkerX(x0, y0, color=XYDrawable._SCAFFOLD_POINT_COLOR)
            end_marker = MarkerX(x, y, color=XYDrawable._SCAFFOLD_POINT_COLOR)
            object_marker = MarkerX(self.x, self.y, color=XYDrawable._SCAFFOLD_OBJECT_COLOR, z=1.0)
            scaffold_scene = Scene([path, start_marker, end_marker, object_marker])
            scaffold_scene = TimeWindowDrawable(scaffold_scene, self.time, self.time + duration)
            scaffold_scene.wait_until(self.time + duration)
        else:
            scaffold_scene = None

        self._manage_time(duration, update_time)

        return scaffold_scene

    def track(
            self,
            other: 'XYDrawable',
            x_offset: tvx.FloatOrTVF = 0.0,
            y_offset: tvx.FloatOrTVF = 0.0,
    ):
        """
        Track the motion of another object at a given offset.
        The offset can be either a constant or time-varying.
        The tracking
        begins at ``self``'s next-action time and continues
        until either the scene ends or another action that
        affects the location is taken.

        See :ref:`track_sample` for sample code.

        Parameters
        ----------
        other
            The object to offset from.
        x_offset
            The offset in the `x` direction.
        y_offset
            The offset in the `y` direction.
        """
        self.x = tvx.cut(self.x, self.time, other.x + x_offset)
        self.y = tvx.cut(self.y, self.time, other.y + y_offset)

    def orbit(
            self,
            other: Union['XYDrawable', Tuple[tvx.FloatOrTVF, tvx.FloatOrTVF]],
            x_amplitude: tvx.FloatOrTVF,
            y_amplitude: tvx.FloatOrTVF,
            orbit_duration: float,
            phase: float = 0.0,
            ccw: bool = False
    ):
        """
        Orbit another object or a point. The orbit motion
        begins at ``self``'s next-action time and continues
        until either the scene ends or another action that
        affects the location is taken.

        See :ref:`orbit_sample` for sample code.

        Parameters
        ----------
        other
            The object to orbit. If it is an :py:class:`~XYDrawable`, the
            center of the orbit will be it's location. If it is a tuple of
            two elements, those elements are the `x` and `y` center of the
            orbit. In either case, the center of the orbit can be time-varying.
        x_amplitude
            The amplitude of the orbit in the `x` direction.
        y_amplitude
            The amplitude of the orbit in the `y` direction.
        orbit_duration
            How long it takes to complete one orbit, in seconds.
        phase
            The phase of the orbit in radians. This determines the location
            of the orbiting object at the beginning of the orbit time.
        ccw
            If ``TRUE`` the orbit is in a counter-clockwise direction. Otherwise,
            it is in a clockwise direction.
        """
        if isinstance(other, XYDrawable):
            cx, cy = other.xy()
        else:
            cx, cy = other

        frequency = 1 / orbit_duration

        x_orbit = cx + tvx.utils.sine_wave(frequency, x_amplitude, phase - np.pi / 2)
        self.x = tvx.cut(self.x, self.time, x_orbit)

        y_wave = tvx.utils.sine_wave(frequency, y_amplitude, phase)
        y_orbit = cy + y_wave if ccw else cy - y_wave
        self.y = tvx.cut(self.y, self.time, y_orbit)

    def quadratic_move_to(
            self, x1: float, y1: float, x2: float, y2: float,
            duration: float, update_time: bool = True,
            scaffold: bool = False
    ) -> Optional[Drawable]:
        """
        Move to a new location over the course of a given amount of time,
        following a quadratic path specified by the current position, a final
        position, and a control point. This is similar to :py:meth:`~move_to`,
        which moves an object along a linear path.

        This method is used in the scripting phase of the object's lifetime
        to schedule it to move from one location on or off-screen to another.
        This is one of the core methods used to produce animations.

        See :ref:`quad_move_to_sample` for sample code.

        The object follows a quadratic path parameterized by :math:`t` which
        varies from 0 to 1 over the duration of motion. The position of
        the object for any given value of :math:`t` is

        .. math::

              x = (1 - t)^2 x_0 + 2 (1 - t) t x_1 + t^2 x_2

              y = (1 - t)^2 y_0 + 2 (1 - t) t y_1 + t^2 y_2

        Note that when :math:`t = 0`, :math:`x = x_0` and :math:`y = y_0`, putting us
        at the starting point. When :math:`t = 1`, :math:`x = x_2` and :math:`y = y_2`, putting us
        at the final point.

        Parameters
        ----------
        x1
            The x coordinate of the control point.
        y1
            The y coordinate of the control point.
        x2
            The x coordinate to move to.
        y2
            The y coordinate to move to.
        duration
            The amount of time, in seconds, the move from the current
            location to the new location should take.
        update_time
            Should the object's time be updated. Normally this is `True`. Making
            it `False` does not change the time, so that other updates can be
            made on the same object at the same time it is moving. For example, :py:meth:`~rotate_to`
            can be called to make the object spin as it moves.
        scaffold
            Should we also generate scaffolding to show the path that the object
            will move along during animation? This is primarily for debugging purposes.
        Returns
        -------
        :py:class:`~Drawable` or ``None``
            ``None`` if ``scaffold`` is ``False`` or a :py:class:`~Drawable` representing
            the scaffolding if the ``scaffold`` is ``True``.
        """
        x0, y0 = self.x, self.y
        xt, yt = tvx.utils.quadratic_path(x0, y0, x1, y1, x2, y2, start=self.time, duration=duration)
        self.x = tvx.cut(self.x, self.time, xt)
        self.y = tvx.cut(self.y, self.time, yt)

        if scaffold:
            path = QuadraticCurveDrawable(x0, y0, x1, y1, x2, y2, color=XYDrawable._SCAFFOLD_PATH_COLOR)
            control_path = PathDrawable([x0, x1, x2], [y0, y1, y2], color=XYDrawable._SCAFFOLD_PATH_COLOR)
            start_marker = MarkerX(x0, y0, color=XYDrawable._SCAFFOLD_POINT_COLOR)
            control_marker = MarkerX(x1, y1, color=XYDrawable._SCAFFOLD_POINT_COLOR)
            end_marker = MarkerX(x2, y2, color=XYDrawable._SCAFFOLD_POINT_COLOR)
            object_marker = MarkerX(self.x, self.y, color=XYDrawable._SCAFFOLD_OBJECT_COLOR, z=1.0)
            scaffold_scene = Scene([
                path, control_path, start_marker, control_marker, end_marker, object_marker
            ])
            scaffold_scene = TimeWindowDrawable(scaffold_scene, self.time, self.time + duration)
            scaffold_scene.wait_until(self.time + duration)
        else:
            scaffold_scene = None

        self._manage_time(duration, update_time)

        return scaffold_scene

    def bezier_move_to(
            self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float,
            duration: float, update_time: bool = True,
            scaffold: bool = False
    ):
        """
        Move to a new location over the course of a given amount of time,
        following a cubic bezier path specified by the current position, a final
        position, and two control points. This is similar to :py:meth:`~move_to`,
        which moves an object along a linear path and :py:meth:`~quadratic_move_to`,
        which moves along a quadratic path.

        This method is used in the scripting phase of the object's lifetime
        to schedule it to move from one location on or off-screen to another.
        This is one of the core methods used to produce animations.

        See :ref:`bezier_move_to_sample` for sample code.

        The object follows a cubic path parameterized by :math:`t` which
        varies from 0 to 1 over the duration of motion. The position of
        the object for any given value of :math:`t` is

        .. math::

              x = (1 - t)^3 x_0 + 3 (1 - t)^2 t x_1 + 3 (1 - t) t^2 x_2 + t^3 x_3

              y = (1 - t)^3 y_0 + 3 (1 - t)^2 t y_1 + 3 (1 - t) t^2 y_2 + t^3 x_3

        Note that when :math:`t = 0`, :math:`x = x_0` and :math:`y = y_0`, putting us
        at the starting point. When :math:`t = 1`, :math:`x = x_3` and :math:`y = y_3`, putting us
        at the final point.

        Parameters
        ----------
        x1
            The x coordinate of the first control point.
        y1
            The y coordinate of the first control point.
        x2
            The x coordinate the second control point.
        y2
            The y coordinate the second control point.
        x3
            The x coordinate to move to.
        y3
            The y coordinate to move to.
        duration
            The amount of time, in seconds, the move from the current
            location to the new location should take.
        update_time
            Should the object's time be updated. Normally this is `True`. Making
            it `False` does not change the time, so that other updates can be
            made on the same object at the same time it is moving. For example, :py:meth:`~rotate_to`
            can be called to make the object spin as it moves.
        scaffold
            Should we also generate scaffolding to show the path that the object
            will move along during animation? This is primarily for debugging purposes.
        Returns
        -------
        :py:class:`~Drawable` or ``None``
            ``None`` if ``scaffold`` is ``False`` or a :py:class:`~Drawable` representing
            the scaffolding if the ``scaffold`` is ``True``.
        """
        x0, y0 = self.x, self.y
        xt, yt = tvx.utils.bezier_path(
            x0, y0, x1, y1, x2, y2, x3, y3, start=self.time, duration=duration
        )
        self.x = tvx.cut(self.x, self.time, xt)
        self.y = tvx.cut(self.y, self.time, yt)

        if scaffold:
            path = BezierDrawable(x0, y0, x1, y1, x2, y2, x3, y3, color=XYDrawable._SCAFFOLD_PATH_COLOR)
            control_path = PathDrawable([x0, x1, x2, x3], [y0, y1, y2, y3], color=XYDrawable._SCAFFOLD_PATH_COLOR)
            start_marker = MarkerX(x0, y0, color=XYDrawable._SCAFFOLD_POINT_COLOR)
            control_marker_1 = MarkerX(x1, y1, color=XYDrawable._SCAFFOLD_POINT_COLOR)
            control_marker_2 = MarkerX(x2, y2, color=XYDrawable._SCAFFOLD_POINT_COLOR)
            end_marker = MarkerX(x3, y3, color=XYDrawable._SCAFFOLD_POINT_COLOR)
            object_marker = MarkerX(self.x, self.y, color=XYDrawable._SCAFFOLD_OBJECT_COLOR, z=1.0)
            scaffold_scene = Scene([
                path, control_path, start_marker, control_marker_1, control_marker_2,
                end_marker, object_marker
            ])
            scaffold_scene = TimeWindowDrawable(scaffold_scene, self.time, self.time + duration)
            scaffold_scene.wait_until(self.time + duration)
        else:
            scaffold_scene = None

        self._manage_time(duration, update_time)

        return scaffold_scene

    def rotate_to(
            self,
            theta: float,
            duration: float,
            update_time: bool = True,
            scaffold: bool = False
    ) -> Optional[Drawable]:
        """
        Rotate to a new angle over the course of a given amount of time.
        This method is used in the scripting phase of the object's lifetime
        to schedule it to rotate the object.
        This is one of the core methods used to produce animations.

        See :ref:`rotate_to_sample` for sample usage.

        Parameters
        ----------
        theta
            The angle to rotate to, expressed in radians. The drawable will be rotated from
            it's current angle
            to this value. When a drawable is first created it's angle is
            normally set to zero, though individual class constructors may allow this
            default to be overridden.
            If you would prefer to specify angles in degrees instead of radians, see
            :py:meth:`~XYDrawable.rotate_to_degrees`.
        duration
            The amount of time, in seconds, the rotation from the current
            angle to the new angle should take.
        update_time
            Should the object's time be updated. Normally this is `True`. Making
            it `False` does not change the time, so that other updates can be
            made on the same object at the same time it is moving. For example, :py:meth:`~move_to`
            can be called to make the object move as it rotates.
        scaffold
            Should we also generate scaffolding to show the path that the object
            will move along during animation? This is primarily for debugging purposes.
        Returns
        -------
        :py:class:`~Drawable` or `None`
            `None` if `scaffold` is `False` or a :py:class:`~Drawable` representing
            the scaffolding if the `scaffold` is `True`.
        """
        theta0 = self.theta
        theta_t = tvx.ramp(theta0, theta, self.time, duration)
        self.theta = tvx.cut(self.theta, self.time, theta_t)

        if scaffold:
            start_marker = MarkerUpArrow(
                self.x, self.y, theta=theta0,
                width=20, height=50,
                color=XYDrawable._SCAFFOLD_POINT_COLOR,
                cross=True,
                z=0.5
            )
            end_marker = MarkerUpArrow(
                self.x, self.y, theta=theta,
                width=20, height=50,
                color=XYDrawable._SCAFFOLD_POINT_COLOR,
                cross=True,
                z=0.5
            )
            object_marker = MarkerUpArrow(
                self.x, self.y, theta=self.theta,
                width=20, height=50,
                color=XYDrawable._SCAFFOLD_OBJECT_COLOR,
                z=1.0
            )
            scaffold_scene = Scene([
                start_marker, end_marker, object_marker
            ])
            scaffold_scene = TimeWindowDrawable(scaffold_scene, self.time, self.time + duration)
            scaffold_scene.wait_until(self.time + duration)
        else:
            scaffold_scene = None

        self._manage_time(duration, update_time)

        return scaffold_scene

    def rotate_to_degrees(
            self,
            degrees: float,
            duration: float,
            update_time: bool = True,
            scaffold: bool = False
    ) -> Optional[Drawable]:
        """
        Rotate the object a certain number of degrees. See :py:meth:`~XYDrawable.rotate_to`
        for more details and an example. The only difference here is that the angle of
        rotation is expressed in degrees instead of radians.

        Note that

        .. code-block:: python

            d.rotate_to_degrees(180, 1.0)

        and

        .. code-block:: python

            import numpy as np

            d.rotate_to(np.pi, 1.0)

        are equivalent because 180 degrees is the same as pi radians.

        See :ref:`rotate_to_degrees_sample` for sample usage.

        Parameters
        ----------
        degrees
            The angle to rotate to, expressed in degrees. The drawable will be rotated from
            it's current angle
            to this value. When a drawable is first created it's angle is
            normally set to zero, though individual class constructors may allow this
            default to be overridden.
            If you would prefer to specify angles in radians instead of degrees, see
            :py:meth:`~XYDrawable.rotate_to`.
        duration
            The amount of time, in seconds, the rotation from the current
            angle to the new angle should take.
        update_time
            Should the object's time be updated. Normally this is ``True``. Making
            it ``False`` does not change the time, so that other updates can be
            made on the same object at the same time it is moving. For example, :py:meth:`~move_to`
            can be called to make the object move as it rotates.
        scaffold
            Should we also generate scaffolding to show the path that the object
            will move along during animation? This is primarily for debugging purposes.
        Returns
        -------
        :py:class:`~Drawable` or ``None``
            ``None`` if ``scaffold`` is ``False`` or a :py:class:`~Drawable` representing
            the scaffolding if the ``scaffold`` is ``True``.
        """
        return self.rotate_to(degrees * _radians_per_degree, duration, update_time, scaffold)

    def current_xy(self, t: float) -> Tuple[float, float]:
        """
        Compute the value of `x` and `y` at time `t`.
        ``self.x`` and ``self.y`` may be time-varying
        values (See :py:mod:`tvx` for details).
        This method returns the floating point values
        computed for the specified time.

        Parameters
        ----------
        t
            The time to evaluate the time-varying values
            ``self.x`` and ``self.y``
        Returns
        -------
        Tuple[float, float]
            A tuple containing the `x` and `y` values at the
            current time.
        """
        x = self.x(t)
        y = self.y(t)

        return x, y


class Background(Drawable):
    """
    A background drawable. Unlike most subclasses of :py:class:`~Drawable`,
    objects of this class have no fixed position or size. Instead, they
    simply fill the entire rendering surface with a color. In order to ensure
    that this is done behind all of the other objects in a :py:class:`~Scene`,
    the default z value for a background is -1. For most other classes, the
    default z is 0.

    Parameters
    ----------
    color
        The color of the background.
    z
        The z value of the background.
    """
    def __init__(self, color: Optional[BaseColor] = None, z: float = -1.0):
        super().__init__(z)
        if color is None:
            color = BACKGROUND
        self._color = color

    def draw(self, ctx: cairo.Context, t: float) -> None:
        with _time_device_drawing():
            with ctx:
                ctx.reset_clip()
                ctx.set_source_rgba(*self._color.tuple(t, alpha_multiplier=float_at_time(self.alpha, t)))
                ctx.paint()


# noinspection PyPropertyDefinition
class BoundedDrawableProtocol(Protocol):
    """
    A protocol for drawables that have a location,
    width, height, and angle of rotation.
    """
    @property
    def x(self) -> tvx.FloatOrTVF: ...

    @property
    def y(self) -> tvx.FloatOrTVF: ...

    @property
    def theta(self) -> tvx.FloatOrTVF: ...

    @property
    def centered(self) -> bool: ...

    @property
    def width(self) -> tvx.FloatOrTVF: ...

    @property
    def height(self) -> tvx.FloatOrTVF: ...


# noinspection PyPropertyDefinition
class AlphaDrawableProtocol(TimekeeperProtocol):
    """
    A protocol for drawables that support alpha.
    """
    @property
    def alpha(self) -> tvx.FloatOrTVF: ...

    @alpha.setter
    def alpha(self, alpha: tvx.FloatOrTVF): ...


class BoundedMixin:
    """
    A mixin that provides common :py:class:`~BoundedDrawableProtocol` functionality.
    """
    def center(self: BoundedDrawableProtocol) -> Tuple[float, float]:
        if self.centered:
            return self.x, self.y
        else:
            return self.x + self.width / 2, self.y + self.height / 2

    def local_xform(self: BoundedDrawableProtocol, t: float) -> cairo.Matrix:
        x = float_at_time(self.x, t)
        y = float_at_time(self.y, t)

        theta = float_at_time(self.theta, t)
        xf_rotate = cairo.Matrix.init_rotate(theta)
        xf_translate = cairo.Matrix(x0=x, y0=y)
        xf = xf_rotate * xf_translate

        if self.centered:
            width = float_at_time(self.width, t)
            height = float_at_time(self.height, t)
            xf_center = cairo.Matrix(x0=-width / 2, y0=-height / 2)
            xf = xf_center * xf

        return xf


@dataclass(init=False)
class Box(XYDrawable, BoundedMixin):
    """
    A rectangular axis-aligned box.

    Parameters
    ----------
    x
        x location of the box
    y
        y location of the box
    width
        width of the box
    height
        height of the box
    color
        color of the line segments around the permimeter
        of the box
    fill_color
        color to fill the box
    line_width
        width of the line segments around the permimeter
        of the box
    z
        z depth of the box
    alpha
        alpha value of the box
    """

    width: tvx.FloatOrTVF = 0.0
    height: tvx.FloatOrTVF = 0.0
    color: BaseColor = TRANSPARENT
    fill_color: BaseColor = TRANSPARENT

    def __init__(
            self,
            x: tvx.FloatOrTVF,
            y: tvx.FloatOrTVF,
            width: tvx.FloatOrTVF,
            height: tvx.FloatOrTVF,
            color: BaseColor,
            fill_color: BaseColor = TRANSPARENT,
            line_width: tvx.FloatOrTVF = 1.0,
            z: tvx.FloatOrTVF = 0.0,
            alpha: tvx.FloatOrTVF = 1.0,
    ):
        super().__init__(x=x, y=y, theta=0.0, z=z, alpha=alpha)
        self.width = width
        self.height = height
        self.color = color
        self.fill_color = fill_color
        self.line_width = line_width

    def draw(self, ctx: cairo.Context, t: float) -> None:
        width = float_at_time(self.width, t)
        if width == 0.0:
            return
        height = float_at_time(self.height, t)
        if height == 0.0:
            return

        x0 = float_at_time(self.x, t)
        y0 = float_at_time(self.y, t)
        x1 = float_at_time(self.x, t) + width
        y1 = float_at_time(self.y, t) + height

        with _time_device_drawing():
            if not self.fill_color.is_transparent():
                ctx.move_to(x0, y0)
                ctx.line_to(x0, y1)
                ctx.line_to(x1, y1)
                ctx.line_to(x1, y0)
                ctx.close_path()
                ctx.set_source_rgba(*self.fill_color.tuple(
                    t, alpha_multiplier=float_at_time(self.alpha, t)
                ))
                ctx.clip()
                ctx.paint()
                ctx.reset_clip()

            if not self.color.is_transparent():
                ctx.set_line_width(float_at_time(self.line_width, t))
                ctx.move_to(x0, y0)
                ctx.line_to(x0, y1)
                ctx.line_to(x1, y1)
                ctx.line_to(x1, y0)
                ctx.close_path()
                ctx.set_source_rgba(*self.color.tuple(
                    t, alpha_multiplier=float_at_time(self.alpha, t)
                ))
                ctx.stroke()

    def rotate_to(
            self,
            theta: float,
            duration: float,
            update_time: bool = True,
            scaffold: bool = False
    ) -> Optional[Drawable]:
        """
        This method is not currently available on this class. Calling it will
        raise an exception.
        """
        raise NotImplementedError("A box is always axis aligned. It cannot be rotated.")

    def contains(self, x: tvx.FloatOrTVF, y: tvx.FloatOrTVF) -> Union[bool, tvx.Tvb]:
        """
        Does this box contain a point?

        Parameters
        ----------
        x
            The x value of the test point. This may be a time-varying
            value.
        y
            The y value of the test point. This may be a time-varying
            value.

        Returns
        -------
            A :py:class:`tvx.Tvb` that evaluates to `True` at any time at which the point
            is inside the box. It evaluates to `False` at any time at which the point
            is not inside the box.
            If the point is on the boundary of the box, it is considered to be
            contained.
        """
        contains_expression = (
            (self.x <= x) & (x <= self.x + self.width) &
            (self.y <= y) & (y <= self.y + self.height)
        )
        return contains_expression


@dataclass(init=False)
class VectorDrawable(XYDrawable, metaclass=ABCMeta):
    """
    The abstract base class for various :py:class:`~Drawable` classes
    that are rendered using lines and/or curves, but not, for example,
    bitmaps. Examples include the various marker classes such as
    :py:class:`~MarkerX` and :py:class:`~MarkerPlus`.

    This class holds basic data that such classes need, such as position,
    angle, alpha, color, and line width. The :py:meth:`~draw` method
    remains abstract. It is up to derived classes to define it.

    This is an abstract class and will not normally be used directly by
    users unless they are implementing a new marker class.

    Parameters
    ----------
    x
        x location
    y
        y location
    theta
        angle of rotation
    color
        color
    line_width
        line width
    z
        depth
    alpha
        alpha
    """
    color: BaseColor = BLACK
    line_width: tvx.FloatOrTVF = 1.0

    def __init__(
            self,
            x: tvx.FloatOrTVF, y: tvx.FloatOrTVF,
            theta: tvx.FloatOrTVF = 0.0,
            color: Optional[BaseColor] = None,
            line_width: tvx.FloatOrTVF = 1.0,
            z: tvx.FloatOrTVF = 0.0,
            alpha: tvx.FloatOrTVF = 1.0,
    ):
        super().__init__(x, y, theta=theta, z=z, alpha=alpha)
        if color is None:
            color = BLACK
        self.color = color
        self.line_width = line_width


@dataclass(init=False)
class PathDrawable(VectorDrawable):
    """
    A class of drawable that renders a piecewise linear
    path. It is currently only used in the rendering of scaffolding.

    Parameters
    ----------
    xs
        The x coordinates of the points on the path.
    ys
        The y coordinates of the points on the path.
    closed
        `True` if we should connect the final point back
        to the first point.
    color
        Color of the line.
    line_width
        Width of the line.
    z
        z order within a scene
    """
    xs: List[tvx.FloatOrTVF] = None
    ys: List[tvx.FloatOrTVF] = None
    closed: bool = False

    def __init__(
            self,
            xs: Iterable[tvx.FloatOrTVF], ys: Iterable[tvx.FloatOrTVF],
            closed: bool = False,
            color: Optional[BaseColor] = None,
            line_width: tvx.FloatOrTVF = 1.0,
            z: tvx.FloatOrTVF = 0.0,
    ):
        xs = list(xs)
        ys = list(ys)

        self._init_done = False
        super().__init__(xs[0], ys[0], 0.0, color, line_width, z)

        self.xs = xs
        self.ys = ys
        self.closed = closed

        self._init_done = True

    @property
    def x(self) -> tvx.FloatOrTVF:
        return self.xs[0]

    @x.setter
    def x(self, value) -> None:
        if self._init_done:
            self.xs[0] = value

    @property
    def y(self) -> tvx.FloatOrTVF:
        return self.ys[0]

    @y.setter
    def y(self, value) -> None:
        if self._init_done:
            self.ys[0] = value

    def draw(self, ctx: cairo.Context, t: float) -> None:
        x = float_at_time(self.x, t)
        y = float_at_time(self.y, t)

        to_x = [float_at_time(x, t) for x in self.xs[1:]]
        to_y = [float_at_time(y, t) for y in self.ys[1:]]

        with _time_device_drawing():
            ctx.set_source_rgba(*self.color.tuple(
                t, alpha_multiplier=float_at_time(self.alpha, t)
            ))
            ctx.set_line_width(self.line_width)

            ctx.move_to(x, y)

            for x, y in zip(to_x, to_y):
                ctx.line_to(x, y)

            if self.closed:
                ctx.close_path()

            ctx.stroke()


@dataclass(init=False)
class BezierDrawable(VectorDrawable):
    """
    A Bezier curve parameterized by four points.
    This can be used to draw a Bezier curve as part
    of an animation. It is also used to generate
    scaffolding for :py:meth:`~XYDrawable.bezier_move_to`.

    Note that, as is the case for most :py:class:`~Drawable`
    classes, the properties that define its shape need not
    be constants. They can be time-varying values, such as
    properties of other :py:class:`~Drawable` objects that
    are in motion.

    See :ref:`partial_motion_linking_samples` for an example
    of the use of this class.

    Parameters
    ----------
    x0
        x coordinate of the start point
    y0
        y coordinate of the start point
    x1
        x coordinate of the first control point
    y1
        y coordinate of the first control point
    x2
        x coordinate of the second control point
    y2
        y coordinate of the second control point
    x3
        x coordinate of the end point
    y3
        y coordinate of the end point
    color
        color of the curve
    line_width
        width of the curve
    z
        z depth
    """

    x0: tvx.FloatOrTVF = 0.0
    y0: tvx.FloatOrTVF = 0.0
    x1: tvx.FloatOrTVF = 0.0
    y1: tvx.FloatOrTVF = 0.0
    x2: tvx.FloatOrTVF = 0.0
    y2: tvx.FloatOrTVF = 0.0
    x3: tvx.FloatOrTVF = 0.0
    y3: tvx.FloatOrTVF = 0.0

    def __init__(
            self,
            x0: tvx.FloatOrTVF, y0: tvx.FloatOrTVF,
            x1: tvx.FloatOrTVF, y1: tvx.FloatOrTVF,
            x2: tvx.FloatOrTVF, y2: tvx.FloatOrTVF,
            x3: tvx.FloatOrTVF, y3: tvx.FloatOrTVF,
            color: Optional[BaseColor] = None,
            line_width: tvx.FloatOrTVF = 1.0,
            z: tvx.FloatOrTVF = 0.0,
    ):
        super().__init__(x0, y0, 0.0, color, line_width, z)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def draw(self, ctx: cairo.Context, t: float) -> None:
        with _time_device_drawing():
            ctx.set_source_rgba(*self.color.tuple(
                t, alpha_multiplier=float_at_time(self.alpha, t)
            ))
            ctx.set_line_width(self.line_width)
            ctx.set_line_cap(cairo.LINE_CAP_ROUND)

            ctx.move_to(float_at_time(self.x, t), float_at_time(self.y, t))
            ctx.curve_to(
                float_at_time(self.x1, t), float_at_time(self.y1, t),
                float_at_time(self.x2, t), float_at_time(self.y2, t),
                float_at_time(self.x3, t), float_at_time(self.y3, t)
            )

            ctx.stroke()


class QuadraticCurveDrawable(BezierDrawable):
    """
    A quadratic curve parameterized by three points.
    This can be used to draw a quadratic curve as part
    of an animation. It is also used to generate
    scaffolding for :py:meth:`~XYDrawable.quadratic_move_to`.

    Note that, as is the case for most :py:class:`~Drawable`
    classes, the properties that define its shape need not
    be constants. They can be time-varying values, such as
    properties of other :py:class:`~Drawable` objects that
    are in motion.

    See :ref:`partial_motion_linking_samples` for an example
    of the use of this class.

    Parameters
    ----------
    x0
        x coordinate of the start point
    y0
        y coordinate of the start point
    x1
        x coordinate of the control point
    y1
        y coordinate of the control point
    x2
        x coordinate of the end point
    y2
        y coordinate of the end point
    color
        color of the curve
    line_width
        width of the curve
    z
        z depth
    """

    def __init__(
            self,
            x0: tvx.FloatOrTVF, y0: tvx.FloatOrTVF,
            x1: tvx.FloatOrTVF, y1: tvx.FloatOrTVF,
            x2: tvx.FloatOrTVF, y2: tvx.FloatOrTVF,
            color: Optional[BaseColor] = None,
            line_width: tvx.FloatOrTVF = 1.0,
            z: tvx.FloatOrTVF = 0.0,
    ):
        # It is possible to create a cubic bezier curve
        # that is actually quadratic and matches a given
        # quadratic curve by putting the two middle control
        # points 2/3 of the way from the end points to the
        # center control point of the quadratic curve.
        super().__init__(
            x0, y0,
            2.0 * x1 / 3.0 + x0 / 3.0, 2.0 * y1 / 3.0 + y0 / 3.0,
            2.0 * x1 / 3.0 + x2 / 3.0, 2.0 * y1 / 3.0 + y2 / 3.0,
            x2, y2,
            color, line_width, z
        )


@dataclass(init=False)
class MarkerBase(VectorDrawable, BoundedMixin, metaclass=ABCMeta):
    """
    The abstract base class for various marker classes, such as :py:class:`~MarkerX`,
    :py:class:`~MarkerPlus` and so on. This holds basic data that markers
    tend to share, such as position, angle, alpha, color, and line width.

    This is an abstract class and will not normally be used directly by
    users unless they are implementing a new marker class.

    The various kinds of markers available are illustrated in the sample
    code in the :ref:`marker_sample` section.

    Parameters
    ----------
    x
        x location
    y
        y location
    width
        width of the marker
    height
        height of the marker
    theta
        angle of the marker
    color
        color of the marker
    line_width
        line width
    z
        depth of the marker
    alpha
        alpha of the marker
    """
    width: tvx.FloatOrTVF = 0.0

    def __init__(
            self,
            x: tvx.FloatOrTVF = 0.0,
            y: tvx.FloatOrTVF = 0.0,
            width: tvx.FloatOrTVF = 16.0,
            height: Optional[tvx.FloatOrTVF] = None,
            theta: tvx.FloatOrTVF = 0.0,
            color: Optional[BaseColor] = None,
            line_width: tvx.FloatOrTVF = 1.0,
            z: tvx.FloatOrTVF = 0.0,
            alpha: tvx.FloatOrTVF = 1.0,
    ):
        super().__init__(x, y, theta, color, line_width, z, alpha=alpha)
        self.width = width
        if height is None:
            height = width
        self.height = height
        self.theta = theta
        self.centered = True

    def _pre_draw(self, ctx: cairo.Context, t: float):
        ctx.set_line_width(self.line_width)
        ctx.set_line_cap(cairo.LINE_CAP_ROUND)
        ctx.set_source_rgba(*self.color.tuple(
            t, alpha_multiplier=float_at_time(self.alpha, t)
        ))


class MarkerPlus(MarkerBase):
    """
    A marker that has the shape of a plus sign (+). See :py:class:`~MarkerBase`
    for more details on markers.

    Parameters
    ----------
    x
        x location
    y
        y location
    width
        width of the marker
    height
        height of the marker
    theta
        angle of the marker
    color
        color of the marker
    line_width
        line width
    z
        depth of the marker
    alpha
        alpha of the marker
    """

    def draw(self, ctx: cairo.Context, t: float) -> None:
        width = float_at_time(self.width, t)
        height = float_at_time(self.height, t)

        with _time_device_drawing():
            self._pre_draw(ctx, t)
            xform = self.local_xform(t)
            with _xform_context(ctx, xform):
                ctx.move_to(0.0, height / 2)
                ctx.line_to(width, height / 2)

                ctx.move_to(width / 2, 0.0)
                ctx.line_to(width / 2, height)

                ctx.stroke()


class MarkerUpArrow(MarkerBase):
    """
    A marker that has the shape of an upward-pointing arrow.
    See :py:class:`~MarkerBase`
    for more details on markers.

    Parameters
    ----------
    x
        x location
    y
        y location
    width
        width of the marker
    height
        height of the marker
    cross
        If `True`, put a small crossing line at the center
    theta
        angle of the marker
    color
        color of the marker
    line_width
        line width
    z
        depth of the marker
    alpha
        alpha of the marker

    """
    def __init__(
            self,
            x: tvx.FloatOrTVF = 0.0,
            y: tvx.FloatOrTVF = 0.0,
            width: tvx.FloatOrTVF = 16.0,
            height: Optional[tvx.FloatOrTVF] = None,
            cross: bool = False,
            theta: tvx.FloatOrTVF = 0.0,
            color: Optional[BaseColor] = None,
            line_width: tvx.FloatOrTVF = 1.0,
            z: tvx.FloatOrTVF = 0.0,
            alpha: tvx.FloatOrTVF = 1.0,
    ):
        if height is None:
            height = 2 * width

        super().__init__(
            x, y, width, height, theta,
            color, line_width, z, alpha
        )
        self._cross = cross

    def draw(self, ctx: cairo.Context, t: float) -> None:
        width = float_at_time(self.width, t)
        height = float_at_time(self.height, t)

        with _time_device_drawing():
            self._pre_draw(ctx, t)
            xform = self.local_xform(t)
            with _xform_context(ctx, xform):
                ctx.move_to(width / 2, 0.0)
                ctx.line_to(width / 2, height)

                ctx.move_to(0.0, height / 4)
                ctx.line_to(width / 2, 0.0)
                ctx.line_to(width, height / 4)

                if self._cross:
                    ctx.move_to(width / 4, height / 2)
                    ctx.line_to(3 * width / 4, height / 2)

                ctx.stroke()


class MarkerX(MarkerBase):
    """
    A marker that is the shape of an X. See :py:class:`~MarkerBase`
    for more details on markers.

    Parameters
    ----------
    x
        x location
    y
        y location
    width
        width of the marker
    height
        height of the marker
    theta
        angle of the marker
    color
        color of the marker
    line_width
        line width
    z
        depth of the marker
    alpha
        alpha of the marker

    """
    def draw(self, ctx: cairo.Context, t: float) -> None:
        width = float_at_time(self.width, t)
        height = float_at_time(self.height, t)

        with _time_device_drawing():
            self._pre_draw(ctx, t)

            with _xform_context(ctx, self.local_xform(t)):
                ctx.move_to(0.0, 0.0)
                ctx.line_to(width, height)

                ctx.move_to(0.0, height)
                ctx.line_to(width, 0.0)

                ctx.stroke()


class MarkerO(MarkerBase):
    """
    A marker that is the shape of circle. See :py:class:`~MarkerBase`
    for more details on markers.

    Parameters
    ----------
    x
        x location
    y
        y location
    width
        width of the marker
    height
        height of the marker
    theta
        angle of the marker
    color
        color of the marker
    line_width
        line width
    z
        depth of the marker
    alpha
        alpha of the marker

    """
    def draw(self, ctx: cairo.Context, t: float) -> None:
        width = float_at_time(self.width, t)
        height = float_at_time(self.height, t)

        with _time_device_drawing():
            self._pre_draw(ctx, t)
            with _xform_context(ctx, self.local_xform(t)):
                ctx.arc(width / 2, height / 2, width / 2, 0.0, 2 * np.pi)
                ctx.stroke()


class MarkerDot(MarkerBase):
    """
    A marker that is the shape of a filled circle. See :py:class:`~MarkerBase`
    for more details on markers.

    Parameters
    ----------
    x
        x location
    y
        y location
    width
        width of the marker
    height
        height of the marker
    theta
        angle of the marker
    color
        color of the marker
    line_width
        line width
    z
        depth of the marker
    alpha
        alpha of the marker

    """

    def draw(self, ctx: cairo.Context, t: float) -> None:
        width = float_at_time(self.width, t)
        height = float_at_time(self.height, t)

        with _time_device_drawing():
            self._pre_draw(ctx, t)
            with _xform_context(ctx, self.local_xform(t)):
                ctx.arc(width / 2, height / 2, width / 2, 0.0, 2 * np.pi)
                ctx.close_path()
                ctx.clip()
                ctx.paint()
                ctx.reset_clip()


@dataclass(init=False)
class _BaseTextDrawable(XYDrawable):
    """
    An abstract base class for drawables that render text.
    """
    font_size: float = 12.0
    color: BaseColor = gewel.color.BLACK

    def __init__(
            self,
            x: tvx.FloatOrTVF,
            y: tvx.FloatOrTVF,
            font_size: float = 12.0,
            color: BaseColor = gewel.color.BLACK,
            z: tvx.FloatOrTVF = 0.0,
            alpha: tvx.FloatOrTVF = 1
    ):
        super().__init__(x, y, 0.0, z, alpha)
        self.font_size = font_size
        self.color = color

    @abstractmethod
    def text(self, t: float) -> str:
        raise NotImplementedError(str(type(self)) + " is abstract.")

    def draw(self, ctx: cairo.Context, t: float) -> None:
        with _time_device_drawing():
            ctx.move_to(float_at_time(self.x, t), float_at_time(self.y, t))
            ctx.set_font_size(self.font_size)
            ctx.set_source_rgba(*self.color.tuple(
                t, alpha_multiplier=float_at_time(self.alpha, t)
            ))
            ctx.show_text(self.text(t))


class ToyTextDrawable(_BaseTextDrawable):
    """
    A very simple and all but deprecated text box that should
    be replaced by :py:class:`~TextBox` in almost all cases.
    """
    def __init__(
            self,
            x: tvx.FloatOrTVF,
            y: tvx.FloatOrTVF,
            text: str,
            font_size: float = 12.0,
            color: BaseColor = gewel.color.BLACK,
            z: tvx.FloatOrTVF = 0.0,
            alpha: tvx.FloatOrTVF = 1
    ):
        super().__init__(x, y, font_size, color, z, alpha)
        self._text = text

    def text(self, t: float) -> str:
        return self._text


class TimeClock(_BaseTextDrawable):
    """
    A drawable that shows the current time.

    This is commonly used while developing and debugging
    animated scenes and then removed before the final version
    is rendered.

    The format of the time shown in `MM:SS.mmm' where `MM` is
    minutes, `SS` is seconds, and `mmm` is milliseconds. If
    the optional ``show_hours`` parameter is set to true, then
    the format is `HH:MM:SS.mmm` where `HH` is hours.

    See :ref:`update_time_samples` for an example of how this
    class is typically used.

    Parameters
    ----------
    x
        x location
    y
        y location
    font_size
        The side of the font to render the time.
    color
        The color of the the time.
    show_hours
        If ``True``, show hours, otherwise don't.
    z
        z depth
    """
    def __init__(self,
                 x: tvx.FloatOrTVF,
                 y: tvx.FloatOrTVF,
                 font_size: float = 12,
                 color: BaseColor = gewel.color.BLACK,
                 show_hours: bool = False,
                 z: tvx.FloatOrTVF = 0.0):
        super().__init__(x, y, font_size, color, z)
        self._show_hours = show_hours

    def text(self, t: float) -> str:
        return tvx.utils.format_time(t, self._show_hours)


class TextJustification(Enum):
    """
    An enumeration for specifying how to justify
    text.
    """
    LEFT = 1  #: Left justified.
    RIGHT = 2  #: Right justified.
    CENTER = 3  #: Centered.


class TextVerticalPosition(Enum):
    """
    An enumeration for specifying the vertical position
    of text.
    """
    TOP = 1  #: Text appears at the top.
    MIDDLE = 2  #: Text appears in the middle.
    BOTTOM = 3  #: Text appears at the botton.


@dataclass(init=False)
class TextBox(ToyTextDrawable):
    """
    A box containing text. The text size, justification, and
    vertical position within the box are all configurable.

    Parameters
    ----------
    text
        The text to put in the box. It may have newlines,
        which will be rendered accordingly. It will also
        wrap at white-space boundaries between words as needed
        to avoid exceeding the width of the box.
    x
        The x position of the text box.
    y
        The y position of the text box.
    width
        The width of the text box.
    height
        The height of the text box.
    font_size
        The font size.
    line_spacing
        Line spacing, relative to font size. For exmaple,
        2.0 means double spaced.
    justification
        Text justification, :py:attr:`~TextJustification.LEFT`,
        :py:attr:`~TextJustification.RIGHT`, or
        :py:attr:`~TextJustification.CENTER`.
    vertical_position
        Vertical position, :py:attr:`TextVerticalPosition.TOP`,
        :py:attr:`TextVerticalPosition.BOTTOM`, or
        :py:attr:`TextVerticalPosition.MIDDLE`.
    color
        Color of the text.
    fill_color
        Color to fill the box with.
    line_color
        Color of the line around the outside of the box.
    line_width
        Width of the line outside the box. 0.0 means no line.
    z
        z depth
    alpha
        alpha
    """
    width: tvx.FloatOrTVF = 0.0
    height: tvx.FloatOrTVF = 0.0
    line_spacing: tvx.FloatOrTVF = 1.2
    justification: TextJustification = TextJustification.LEFT
    vertical_position: TextVerticalPosition = TextVerticalPosition.TOP

    def __init__(
            self,
            text: str,
            x: tvx.FloatOrTVF,
            y: tvx.FloatOrTVF,
            width: tvx.FloatOrTVF,
            height: tvx.FloatOrTVF,
            font_size: float = 12.0,
            line_spacing: tvx.FloatOrTVF = 1.2,
            justification: TextJustification = TextJustification.LEFT,
            vertical_position: TextVerticalPosition = TextVerticalPosition.TOP,
            color: BaseColor = gewel.color.BLACK,
            fill_color: BaseColor = TRANSPARENT,
            line_color: BaseColor = TRANSPARENT,
            line_width: tvx.FloatOrTVF = 1,
            z: tvx.FloatOrTVF = 0.0,
            alpha: tvx.FloatOrTVF = 1
    ):
        super().__init__(x, y, text, font_size, color, z, alpha)
        self.width = width
        self.height = height
        self.line_spacing = line_spacing
        self.justification = justification
        self.vertical_position = vertical_position
        self.fill_color = fill_color
        self.line_color = line_color
        self.line_width = line_width

        # If we draw repeatedly at the same width,
        # we're likely to not have to compute the lines
        # to draw all over again.
        #
        # TODO: need to recompute splits if text size changes.
        self._last_draw_location = (None, None)
        self._last_draw_width = None
        self._line_splits_for_width = None

    def draw(self, ctx: cairo.Context, t: float) -> None:
        box_height = float_at_time(self.height, t)
        if box_height == 0.0:
            return
        box_width = float_at_time(self.width, t)
        if box_width == 0.0:
            return

        x, y = float_at_time(self.x, t), float_at_time(self.y, t)
        x1, y1 = x + box_width, y + box_height

        with _time_device_drawing():
            if box_width != self._last_draw_width or (x, y) != self._last_draw_location:
                font_size = float_at_time(self.font_size, t)

                self._line_splits_for_width = walk_text(
                    ctx, self.text(t),
                    x, y, box_width, font_size, self.line_spacing,
                    self.justification
                )
                self._last_draw_width = box_width
                self._last_draw_location = (x, y)

            if self.fill_color is not None:
                if not self.fill_color.is_transparent():
                    ctx.move_to(x, y)
                    ctx.line_to(x, y1)
                    ctx.line_to(x1, y1)
                    ctx.line_to(x1, y)
                    ctx.close_path()
                    ctx.set_source_rgba(*self.fill_color.tuple(
                        t, alpha_multiplier=float_at_time(self.alpha, t)
                    ))
                    ctx.clip()
                    ctx.paint()
                    ctx.reset_clip()

                if not self.line_color.is_transparent():
                    ctx.set_line_width(float_at_time(self.line_width, t))
                    ctx.move_to(x, y)
                    ctx.line_to(x, y1)
                    ctx.line_to(x1, y1)
                    ctx.line_to(x1, y)
                    ctx.close_path()
                    ctx.set_source_rgba(*self.line_color.tuple(
                        t, alpha_multiplier=float_at_time(self.alpha, t)
                    ))
                    ctx.stroke()

            if not self.color.is_transparent():
                # Figure out a top margin based on vertical
                # position.
                font_size = float_at_time(self.font_size, t)
                text_height = (font_size + (len(self._line_splits_for_width) - 1) *
                               self.line_spacing * font_size)
                if self.vertical_position == TextVerticalPosition.MIDDLE:
                    top_margin = (self.height - text_height - font_size) / 2
                elif self.vertical_position == TextVerticalPosition.BOTTOM:
                    top_margin = self.height - text_height - font_size
                else:
                    top_margin = 0.0

                ctx.set_font_size(self.font_size)
                ctx.set_source_rgba(*self.color.tuple(
                    t, alpha_multiplier=float_at_time(self.alpha, t)
                ))
                for line_x, line_y, line in self._line_splits_for_width:
                    if line is not None:
                        ctx.move_to(line_x, line_y + top_margin)
                        ctx.show_text(line)


def walk_text(
        ctx: cairo.Context,
        text: str,
        x: float, y: float,
        box_width: float,
        font_size: float,
        line_spacing: float,
        justification: TextJustification,
) -> List[Tuple[float, float, Optional[str]]]:
    """
    A subroutine for chopping strings into lines to
    be rendered. This is used as a subroutine by
    text-rendering classes such as :py:class:`~TextBox`
    and :py:class:`~Teleprompter`. It is only public
    so that code in :py:mod:`gewel.contrib` can
    access it when needed.

    Parameters
    ----------
    ctx
        The low-level drawing context we intend to render
        to.
    text
        The text to be rendered.
    x
        The x location.
    y
        The y location.
    box_width
        The width of the text in pixels. Lines will be
        broken so that rendered text does not exceed this
        width.
    font_size
        Font size.
    line_spacing
        Line spacing (relative to the font size, e.g. 2.0
        means double spaced).
    justification
        The justification.

    Returns
    -------
    List[Tuple[float, float, Optional[str]]]
        A list of tuples, one per line of text. Each tuple has
        three elements: the x position of the line, the y position
        of the line, and the text that goes on that line.
    """
    line_y = y + line_spacing * font_size

    ctx.set_font_size(font_size)

    line_count = 0
    drawable_lines = []

    lines = text.split('\n')
    for line in lines:
        words = line.split()
        if len(words) > 0:
            line_start = line.find(words[0])
            ii = 0
            while ii < len(words):
                line_end = line_start
                selected_width = 0
                while ii < len(words):
                    next_end = line.find(words[ii], line_end) + len(words[ii])
                    x_bearing, y_bearing, width, height, x_advance, y_advance = \
                        ctx.text_extents(line[:next_end])
                    if width > box_width:
                        if line_end == line_start:
                            # A single long word was wider than the box.
                            selected_width = width
                            ii = ii + 1
                            line_end = next_end
                        break
                    else:
                        selected_width = width
                        ii = ii + 1
                        line_end = next_end

                drawable_line = line[line_start:line_end]
                if justification == TextJustification.LEFT:
                    x_offset = 0
                elif justification == TextJustification.CENTER:
                    x_offset = (box_width - selected_width) / 2
                else:  # justification == TextJustification.RIGHT:
                    x_offset = box_width - selected_width

                line_x = x + x_offset

                drawable_lines.append((line_x, line_y, drawable_line))

                line_count = line_count + 1
                line_y = y + (line_count + 1) * line_spacing * font_size

                line = str(line[line_end:])
                if ii < len(words):
                    line_start = line.find(words[ii])
        else:
            # Blank line.
            drawable_lines.append((x, line_y, None))
            line_count = line_count + 1
            line_y = y + (line_count + 1) * line_spacing * font_size

    return drawable_lines


@dataclass(init=False)
class TransformedDrawable(Drawable):
    """
    A drawable that is a transformed version of another. Typically
    constructed by calling :py:meth:`~Drawable.transformed`.

    Parameters
    ----------
    drawable
        The drawable to rotate.
    xx
        Element of the matrix.
    yx
        Element of the matrix.
    xy
        Element of the matrix.
    yy
        Element of the matrix.
    x0
        Translation in `x`
    y0
        Translation in `y`
    z
        The z depth of the new drawable.
    """

    drawable: Drawable = None
    xx: tvx.FloatOrTVF = 1.0
    yx: tvx.FloatOrTVF = 0.0
    xy: tvx.FloatOrTVF = 0.0
    yy: tvx.FloatOrTVF = 1.0
    x0: tvx.FloatOrTVF = 0.0
    y0: tvx.FloatOrTVF = 0.0

    def __init__(
            self,
            drawable: Drawable,
            xx: tvx.FloatOrTVF = 1.0,
            yx: tvx.FloatOrTVF = 0.0,
            xy: tvx.FloatOrTVF = 0.0,
            yy: tvx.FloatOrTVF = 1.0,
            x0: tvx.FloatOrTVF = 0.0,
            y0: tvx.FloatOrTVF = 0.0,
            z: tvx.FloatOrTVF = 0.0,
    ):
        super().__init__(z=z)
        self.drawable = drawable
        self.xx = xx
        self.yx = yx
        self.xy = xy
        self.yy = yy
        self.x0 = x0
        self.y0 = y0

    def draw(self, ctx: cairo.Context, t: float) -> None:
        xform = cairo.Matrix(
            xx=float_at_time(self.xx, t), yx=float_at_time(self.yx, t),
            xy=float_at_time(self.xy, t), yy=float_at_time(self.yy, t),
            x0=float_at_time(self.x0, t), y0=float_at_time(self.y0, t),
        )
        with _xform_context(ctx, xform):
            self.drawable.draw(ctx, t)


@dataclass(init=False)
class RotatedDrawable(Drawable):
    """
    A drawable that is a rotated version of another. Typically
    constructed by calling :py:meth:`~Drawable.rotated`
    or :py:meth:`~Drawable.rotated_degrees`.

    Parameters
    ----------
    drawable
        The drawable to rotate.
    radians
        How far to rotate the original drawable.
    z
        The z depth of the new drawable.
    """
    drawable: Drawable = None
    radians: tvx.FloatOrTVF = 0.0

    def __init__(self, drawable: Drawable, radians: tvx.FloatOrTVF, z: tvx.FloatOrTVF = 0.0):
        super().__init__(z=z)
        self.drawable = drawable
        self.radians = radians

    def draw(self, ctx: cairo.Context, t: float) -> None:
        xform = cairo.Matrix.init_rotate(float_at_time(self.radians, t))
        with _xform_context(ctx, xform):
            self.drawable.draw(ctx, t)


@dataclass(init=False)
class TranslatedDrawable(Drawable):
    """
    A drawable that is a shifted version of another. Typically
    constructed by calling :py:meth:`~Drawable.translated`.

    Parameters
    ----------
    drawable
        The drawable to translate.
    dx
        How far to translate the original drawable in the `x` direction.
    dy
        How far to translate the original drawable in the `y` direction.
    z
        The z depth of the new drawable.
    """
    drawable: Drawable = None
    dx: tvx.FloatOrTVF = 0.0
    dy: tvx.FloatOrTVF = 0.0

    def __init__(self, drawable: Drawable, dx: tvx.FloatOrTVF = 0.0, dy: tvx.FloatOrTVF = 0.0, z: tvx.FloatOrTVF = 0.0):
        super().__init__(z=z)
        self.drawable = drawable
        self.dx = dx
        self.dy = dy

    def draw(self, ctx: cairo.Context, t: float) -> None:
        xform = cairo.Matrix(x0=float_at_time(self.dx, t), y0=float_at_time(self.dy, t))
        with _xform_context(ctx, xform):
            self.drawable.draw(ctx, t)


class PngDrawable(XYDrawable, BoundedMixin):
    """
    A :py:class:`~Drawable` that renders a the contents
    of a png file.

    See :ref:`png_sample` for an example of how to use
    this class.

    Parameters
    ----------
    png_path
        The path to load the png from the local file system.
    x
        The x coordinate of the location at which to render
        the image.
    y
        The y coordinate of the location at which to render
        the image.
    theta
        The angle at which to render the image. In radians.
    centered
        If `True` then `x` and `y` specify the location of
        the center of the image. If `False`, they specify
        the location of the top left corner.
    z
        The depth at which to render. Drawables with higher `z` are
        rendered on top of those with lower `z`.
    """
    def __init__(
            self,
            png_path: str,
            x: tvx.FloatOrTVF = 0.0,
            y: tvx.FloatOrTVF = 0.0,
            theta: tvx.FloatOrTVF = 0.0,
            centered: bool = True,
            z: tvx.FloatOrTVF = 0.0
    ):
        image_surface = cairo.ImageSurface.create_from_png(png_path)
        super().__init__(x, y, theta, z)
        self.width = image_surface.get_width()
        self.height = image_surface.get_height()
        self.centered = centered
        self._image_surface = image_surface

    def draw(self, ctx: cairo.Context, t: float):
        alpha = float_at_time(self.alpha, t)
        with _time_device_drawing():
            xform = self.local_xform(t)
            with _xform_context(ctx, xform):
                ctx.set_source_surface(self._image_surface)
                ctx.paint_with_alpha(alpha)


@dataclass(init=False)
class ClippedDrawable(XYDrawable):
    """
    A drawable that is a clipped version of another drawable.
    The clipping region is an axis-aligned rectangle.

    This class is used by :py:class:`~Teleprompter` to clip
    the scrolling text to the bounds of the teleprompter.

    Parameters
    ----------
    d
        The drawable to clip.
    x
        x position of the clipping region
    y
        y position of the clipping region
    width
        width of the clipping region
    height
        height of the clipping region
    z
        z depth
    """
    d: Drawable = None
    width: tvx.FloatOrTVF = 0.0
    height: tvx.FloatOrTVF = 0.0

    def __init__(
            self,
            d: Drawable,
            x: tvx.FloatOrTVF,
            y: tvx.FloatOrTVF,
            width: tvx.FloatOrTVF,
            height: tvx.FloatOrTVF,
            z: tvx.FloatOrTVF = 0.0
    ):
        super().__init__(x, y, z)
        self.d = d
        self.width = width
        self.height = height

    def draw(self, ctx: cairo.Context, t: float) -> None:
        width = float_at_time(self.width, t)
        if width == 0.0:
            return
        height = float_at_time(self.height, t)
        if height == 0.0:
            return
        x = float_at_time(self.x, t)
        y = float_at_time(self.y, t)
        with _clipped_rectangle_context(ctx, x, y, x + width, y + height) as ctx:
            self.d.draw(ctx, t)


class BaseScene(Drawable, metaclass=ABCMeta):
    """
    A base class for :py:class:`~Scene`, :py:class:`~SceneSequence`,
    and :py:class:`~ClipDrawable` that provides a little bit of shared
    base functionality.

    :meta private:
    """
    def __init__(
            self,
            render_width: int = 640,
            render_height: int = 480,
            z: tvx.FloatOrTVF = 0.0
    ):
        super().__init__(z=z)
        self._render_height = render_height
        self._render_width = render_width

    @property
    def render_width(self) -> int:
        return self._render_width

    @property
    def render_height(self) -> int:
        return self._render_height

    def __repr__(self):
        _scene_widget(self)
        return "Scene - {:d} x {:d}".format(self._render_width, self._render_height)


class Scene(BaseScene):
    """
    A scene is a collection of :py:class:`~Drawable` objects.
    Normally, a scene is created at the very end of the scripting
    phase of creating an animation. It is then previewed with a
    :py:class:`~gewel.player.Player` or rendered to a file
    with a :py:class:`gewel.record.Mp4Recorder` or similar.

    See any of the sample code snippets in this API reference that
    generate animations for uses of :py:class:`~Scene`. For example,
    :py:meth:`~XYDrawable.move_to` or
    :py:meth:`~XYDrawable.rotate_to`.

    Parameters
    ----------
    drawables
        The drawables that are in the scene.
    render_width
        The width of the scene when rendered, in pixels.
    render_height
        The height of the scene when rendered, in pixels.
    z
        The z order of the scene, in case it is rendered
        along with other scenes in a compound scene. Rarely
        used.
    """
    def __init__(
            self,
            drawables: Iterable[Drawable],
            render_width: int = 640,
            render_height: int = 480,
            z: tvx.FloatOrTVF = 0.0
    ):
        super().__init__(render_width, render_height, z)
        self._drawables: List[Drawable] = list(drawables)
        self.wait_for(self._drawables)
        self._render_height = render_height
        self._render_width = render_width

    def draw(self, ctx: cairo.Context, t: float) -> None:
        # Note that we have to sort each time we draw, rather
        # than storing in alpha sorted list since z can vary with
        # time.
        for drawable in sorted(self._drawables, key=lambda d: float_at_time(d.z, t)):
            drawable.draw(ctx, t)

    def add(self, drawable: Drawable) -> None:
        self._drawables.append(drawable)
        self.wait_for(drawable)

    def pop(self, index: int = -1) -> Drawable:
        d = self._drawables.pop(index)

        self.set_time(0.0)
        if len(self._drawables):
            if d.time == self.time:
                self.wait_until(max([d.time for d in self._drawables]))

        return d

    def at(self, time: float) -> 'Frame':
        """
        The scene at a specific instance in time. Normally this is
        used to render the scene at the specified time, typically
        inside a notebook where it will automatically render as the
        output.

        Parameters
        ----------
        time
            The time at which we want to view the scene.
        Returns
        -------
        Frame
            The scene at time ``t``.
        """
        return Frame(self, time)

    def __getitem__(self, item: Union[float, slice]) -> 'ClipDrawable':
        """
        Get the frame at a specific time or a clip
        covering a range from start to end time.

        Parameters
        ----------
        time
            Either a float, in which case the return value is a
            frame at the given time, or a slice of the form ``start:end``,
            in which case the return value is a clip of the scene covering
            that range of time.
        Returns
        -------
        Union[ClipDrawable, Clip]
            A frame or a clip, depending on whether the argument was
            a float or a slice.
        """
        if isinstance(item, slice):
            return ClipDrawable(self, item.start, item.stop)
        else:
            return Frame(self, item)


@dataclass(init=False)
class ClipDrawable(Drawable):
    """
    A scene that is a clip of another scene. If ``start`` is
    negative or ``stop`` is greater than the length of the
    scene, behavior is undefined.

    Parameters
    ----------
    base_drawable
        The :py:class:`~Drawable` we want a clip of.
    start
        The start time of the clip.
    stop
        The end time of the clip.
    z
        The z order for the clip.
    """
    base_drawable: Drawable = None
    start: float = 0.0
    stop: float = 0.0

    def __init__(self, base_drawable: Drawable, start: float, stop: float, z: Optional[float] = None):
        if z is None:
            z = base_drawable.z

        super().__init__(z=z, alpha=1.0)

        self.base_drawable = base_drawable
        self.start = start
        self.stop = stop

        self.set_time(max([0.0, min(stop, base_drawable.time) - self.start]))

    def draw(self, ctx: cairo.Context, t: float) -> None:
        scene_time = t + self.start
        self.base_drawable.draw(ctx, scene_time)


class Frame:
    """
    A single frame in a scene. Normally constructed using
    ``scene[frame_time]``. See :py:meth:`~Scene.__getitem__`.

    Typically these are used inside notebooks to render an
    image of a scene at a given time.

    Parameters
    ----------
    scene
        The scene.
    at_time
        The time for the frame.
    """
    def __init__(self, scene: BaseScene, at_time: float):
        self._scene = scene
        self._at_time = at_time

    def to_png(self, target: Union[str, IO, None] = None) -> Optional[BytesIO]:
        width = self._scene.render_width
        height = self._scene.render_height
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
        ctx = cairo.Context(surface)

        self._scene.draw(ctx, self._at_time)

        surface.flush()

        return surface.write_to_png(target)

    def __repr__(self):
        png = self.to_png()
        IPython.display.display(IPython.display.Image(png))

        return "Scene at {:}".format(tvx.utils.format_time(self._at_time))


def _scene_widget(scene: BaseScene):
    width = scene.render_width
    height = scene.render_height
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)

    @widgets.interact(
        time=widgets.FloatSlider(
            min=-0, max=scene.time, step=1.0 / 30, value=0.0,
            description="Time (sec.):",
            layout=widgets.Layout(width='600px')
        )
    )
    def _show_image_for_time(time=(0, scene.time, 1.0 / 30)):
        scene.draw(ctx, time)

        surface.flush()
        png = surface.write_to_png()
        IPython.display.display(IPython.display.Image(png))

    return _show_image_for_time


class SceneSequence(BaseScene):
    def __init__(
            self,
            scenes: Iterable[Scene],
            render_width: int = 640,
            render_height: int = 480,
            z: tvx.FloatOrTVF = 0.0,
    ):
        super().__init__(render_width, render_height, z)
        self._scenes = []
        self._scene_start_times = [0.0]
        for scene in scenes:
            self.append(scene)

    def append(self, scene: Scene):
        self._scenes.append(scene)
        self._scene_start_times.append(self._scene_start_times[-1] + scene.time)
        self.wait(scene.time)

    def draw(self, ctx: cairo.Context, t: float) -> None:
        index = bisect.bisect_left(self._scene_start_times, t) - 1

        # If t <= 0, we could have ended up at -1.
        index = max(index, 0)
        # If t is beyond the last scene use the end
        # of the last scene.
        index = min(index, len(self._scenes) - 1)

        self._scenes[index].draw(ctx, t - self._scene_start_times[index])

    def __len__(self):
        return len(self._scenes)


class Teleprompter(XYDrawable):
    """
    A class that animates scrolling text inside a rectangular box.
    The typical use case is to script a voiceover that goes along
    with whatever other objects are in the animation. The voiceover
    artist can then read along with the teleprompter and record
    their voice, which can then be added to the animation.
    The teleprompter can be left in to make the video more accessible.

    Teleprompters
    can be kept in sync with other objects in the animation by
    interleaving calls to :py:meth:`~Teleprompter.add_text` with
    calls to :py:meth:`~Drawable:wait_for`,
    :py:func:`~gewel.draw.sync` and related synchronization
    calls.

    See :ref:`teleprompter_sample` for an example that uses a
    teleprompter.
    """
    def __init__(
            self,
            x: tvx.FloatOrTVF, y: tvx.FloatOrTVF,
            width: tvx.FloatOrTVF, height: tvx.FloatOrTVF,
            font_size: float = 12.0,
            line_spacing: tvx.FloatOrTVF = 1.5,
            lines_per_second: float = 0.8,
            color: BaseColor = gewel.color.BLACK,
            fill_color: BaseColor = TRANSPARENT,
            line_color: BaseColor = TRANSPARENT,
            line_width: tvx.FloatOrTVF = 1,
            z: tvx.FloatOrTVF = 0.0
    ):
        super().__init__(x, y, z)
        self._width = width
        self._height = height
        self._font_size = font_size
        self._line_spacing = line_spacing
        self._lines_per_second = lines_per_second
        self._color = color
        self._scroll_velocity = lines_per_second * line_spacing * font_size
        self.set_time(0.0)

        self._background = Box(
            x, y, width, height,
            color=gewel.color.TRANSPARENT,
            fill_color=fill_color,
            line_width=0.0,
            z=-1.0
        )
        self._text_collection = Scene([], z=0.0)
        self._border = Box(x, y, width, height, color=line_color, line_width=line_width, z=1.0)

        scrolling_text = TranslatedDrawable(
            self._text_collection,
            dy=-self._scroll_velocity * tvx.time()
        )

        clipped_scrolling_text = ClippedDrawable(scrolling_text, x, y, width, height)

        self._scene = Scene([self._background, clipped_scrolling_text, self._border])

        # A dummy context for when we need to check text
        # extents to determine how many lines will be
        # needed to render some text.
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 64, 64)
        self._dummy_ctx = cairo.Context(surface)

    @property
    def time(self):
        return self._time

    @staticmethod
    def _script_to_text(script: str) -> str:
        # Drop leading/trailing white space.
        text = re.sub(r'(^[ \t\n]+)|([ \t\n]+$)', '', script)

        # Wrap paragraphs into a single line.
        text = re.sub(r'(^|[^ \t\n])[ \t]*\n[ \t]*([^ \t\n]|$)', r'\g<1> \g<2>', text)

        # Remove multiple newlines and white space between paragraphs.
        text = re.sub(r'([ \t]*\n)([ \t]*\n[ \t]*)+', '\n', text)

        return text

    def add_script(self, script: str, at_time: Optional[float] = None) -> None:
        """
        Add to the the script in the teleprompter. This is like :py:meth:`~add_text`
        except that it does some basic formatting. It is normally called with a
        triple-quoted multi-line string. The formatting that is done is:

        #. Leading and trailing whitespace is dropped.
        #. Multiple consecutive lines not separated by a blank line are converted into
           a single paragraph. This is useful because it lets you write paragraphs
           without worrying about the width of the text box they will appear in and
           where you need to wrap them.
        #. Multiple blank lines between paragraphs are converted into a single paragraph
           break.

        Parameters
        ----------
        script
            The text to format and render into the teleprompter.
        at_time
            Optional time at which to start the text. If missing use the current
            time of the teleprompter, which is the time the last text was rendered
            or the time the teleprompter last waited for.
        """
        self.add_text(self._script_to_text(script), at_time)

    def add_text(self, text: str, at_time: Optional[float] = None) -> None:
        """
        Add unformatted text to the teleprompter. In most cases, you should
        use :py:meth:~`add_script` instead.

        Parameters
        ----------
        text
            The text to add.
        at_time
            Optional time at which to start the text. If missing use the current
            time of the teleprompter, which is the time the last text was rendered
            or the time the teleprompter last waited for.
        """
        if at_time is None:
            at_time = self.time

        x = self.x
        y = self.y + self._scroll_velocity * at_time
        # Offset the text so text at time zero starts about 1/3 from the top.
        y = y + self._height / 3.0

        text_box = TextBox(
            text, x=x, y=y,
            width=self._width, height=self._height,
            font_size=self._font_size,
            line_spacing=self._line_spacing,
            color=self._color
        )

        self._text_collection.add(text_box)

        lines = walk_text(
            self._dummy_ctx, text,
            x, y, self._width,
            self._font_size, self._line_spacing,
            TextJustification.LEFT
        )

        self.set_time(at_time + len(lines) / self._lines_per_second)

    def draw(self, ctx: cairo.Context, t: float) -> None:
        self._scene.draw(ctx, t)


@dataclass(init=False)
class ColorMapBox(XYDrawable, BoundedMixin):
    width: tvx.FloatOrTVF = 0.0
    height: tvx.FloatOrTVF = 0.0
    color_map: ColorMap = TRANSPARENT
    steps: int = 32
    border_color: BaseColor = TRANSPARENT

    def __init__(
            self,
            x: tvx.FloatOrTVF,
            y: tvx.FloatOrTVF,
            width: tvx.FloatOrTVF,
            height: tvx.FloatOrTVF,
            color_map: ColorMap,
            steps: int = 32,
            border_color: BaseColor = TRANSPARENT,
            vertical: bool = True,
            line_width: tvx.FloatOrTVF = 1.0,
            theta: tvx.FloatOrTVF = 0.0,
            z: tvx.FloatOrTVF = 0.0,
            alpha: tvx.FloatOrTVF = 1.0,
    ):
        super().__init__(x=x, y=y, theta=theta, z=z, alpha=alpha)
        self.width = width
        self.height = height
        self.color_map = color_map
        self.steps = steps
        self._vertical = vertical
        self.border_color = border_color
        self.line_width = line_width
        self.centered = False

    @property
    def vertical(self) -> bool:
        return self._vertical

    def draw(self, ctx: cairo.Context, t: float) -> None:
        width = float_at_time(self.width, t)
        if width == 0.0:
            return
        height = float_at_time(self.height, t)
        if height == 0.0:
            return

        if self._vertical:
            transpose_xform = cairo.Matrix()
        else:
            # We are horizontal, so we'll transpose
            # x and y before we do any drawing.
            transpose_xform = cairo.Matrix(xx=0, xy=1, yx=1, yy=0)

            width, height = height, width

        # Now we can draw as if we are vertical

        with _xform_context(ctx, self.local_xform(t)):
            with _xform_context(ctx, transpose_xform):
                # There are self.steps color positions based on the midpoints of
                # self.steps segments, each of which is the same color. There are
                # self.steps + 1 values of y that bound the regions where these
                # are drawn.

                color_positions = np.linspace(
                    0.5 / self.steps,
                    1 - 0.5 / self.steps,
                    self.steps
                )
                ys = np.linspace(0.0, height, self.steps + 1)

                original_position = self.color_map.position

                x0 = 0.0
                x1 = width

                with _time_device_drawing():
                    for y0, y1, color_position in zip(ys[:-1], ys[1:], color_positions):
                        self.color_map.position = color_position
                        color_tuple = self.color_map.tuple(t, alpha_multiplier=self.alpha)

                        ctx.move_to(x0, y0 - 0.5)
                        ctx.line_to(x0, y1 + 0.5)
                        ctx.line_to(x1, y1 + 0.5)
                        ctx.line_to(x1, y0 - 0.5)
                        ctx.close_path()
                        ctx.set_source_rgba(*color_tuple)
                        ctx.clip()
                        ctx.paint()
                        ctx.reset_clip()

                    self.color_map.position = original_position

                    if not self.border_color.is_transparent():
                        ctx.set_line_width(float_at_time(self.line_width, t))
                        ctx.move_to(x0, ys[0])
                        ctx.line_to(x0, ys[-1])
                        ctx.line_to(x1, ys[-1])
                        ctx.line_to(x1, ys[0])
                        ctx.close_path()
                        ctx.set_source_rgba(*self.border_color.tuple(
                            t, alpha_multiplier=float_at_time(self.alpha, t)
                        ))
                        ctx.stroke()


# Bring gewel._timekeeper functions into this package
# since this is the public place from which they will be used.
# Note that we also narrow the type signatures to take
# Drawables.

def sync(drawables: Iterable[Drawable]) -> None:
    """
    Ensure that two or more :py:class:`~Drawable` objects
    are in sync, meaning that all of them will wait for
    whichever has the latest completing action before any
    takes a next action.

    Parameters
    ----------
    drawables
        The drawables to syncronize.

    Returns
    -------

    """
    gewel._timekeeper.sync(drawables)


def all_wait_for(waiters: Iterable[Drawable], waited_on: Drawable) -> None:
    """
    Have a group of :py:class:`~Drawable` objects wait on a single
    :py:class:`~Drawable`. This is mostly just used as a
    syntactic shortcut for cases where we want to synchronize
    a collection of :py:class:`~Drawable` objects so that they
    don't take their next action until some single :py:class:`~Drawable`
    has completed it's current action. The call

    .. code-block:: python

        all_wait_for([d1, d2, d3], d0)

    is equivalent to

    .. code-block:: python

        for d in [d1, d2, d3]:
            d.wait_for(d0)

    Parameters
    ----------
    waiters
        The :py:class:`~Drawable` objects that should wait.
    waited_on
        The :py:class:`~Drawable` to wait on.

    Returns
    -------

    """
    gewel._timekeeper.all_wait_for(waiters, waited_on)
