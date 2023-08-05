from dataclasses import dataclass
from typing import Optional, Iterable

import cairocffi as cairo
import numpy as np

import tvx
from gewel.color import ColorMap, DARK_GRAY, TRANSPARENT, BaseColor
from gewel.draw import XYDrawable, BoundedMixin, _xform_context, walk_text, TextJustification
from tvx import float_at_time


@dataclass(init=False)
class TvfChartDrawable(XYDrawable, BoundedMixin):
    width: tvx.FloatOrTVF = 0.0
    height: tvx.FloatOrTVF = 0.0
    min_time: float = 0.0
    max_time: float = 1.0
    min_value: Optional[float] = None
    max_value: Optional[float] = None
    time_ticks: Optional[Iterable[float]] = None
    value_ticks: Optional[Iterable[float]] = None
    line_width: tvx.FloatOrTVF = 1.0
    line_color: ColorMap = DARK_GRAY
    fill_color: ColorMap = TRANSPARENT
    border_width: tvx.FloatOrTVF = 1.0
    border_color: BaseColor = TRANSPARENT
    title: Optional[str] = None
    steps: int = 100

    def __init__(
        self,
            tvf: tvx.Tvf,
            x: tvx.FloatOrTVF,
            y: tvx.FloatOrTVF,
            width: tvx.FloatOrTVF,
            height: tvx.FloatOrTVF,
            min_time: float = 0.0,
            max_time: float = 1.0,
            min_value: Optional[float] = None,
            max_value: Optional[float] = None,
            time_ticks: Optional[Iterable[float]] = None,
            value_ticks: Optional[Iterable[float]] = None,
            line_width: tvx.FloatOrTVF = 1.0,
            line_color: ColorMap = DARK_GRAY,
            fill_color: ColorMap = TRANSPARENT,
            border_width: tvx.FloatOrTVF = 1.0,
            border_color: BaseColor = TRANSPARENT,
            title: Optional[str] = None,
            steps: int = 100,
            theta: tvx.FloatOrTVF = 0.0,
            z: tvx.FloatOrTVF = 0.0,
            alpha: tvx.FloatOrTVF = 1.0,
    ):
        super().__init__(x=x, y=y, theta=theta, z=z, alpha=alpha)
        self._tvf = tvf
        self.width = width
        self.height = height
        self.min_time = min_time
        self.max_time = max_time
        self.min_value = min_value
        self.max_value = max_value
        if time_ticks is not None:
            self.time_ticks = list(time_ticks)
        if value_ticks is not None:
            self.value_ticks = list(value_ticks)
        self.line_width = line_width
        self.line_color = line_color
        self.fill_color = fill_color
        self.border_width = border_width
        self.border_color = border_color
        self.title = title
        self.steps = steps
        self.centered = False

    def draw(self, ctx: cairo.Context, t: float) -> None:
        alpha = float_at_time(self.alpha, t)
        if alpha == 0.0:
            return

        width = float_at_time(self.width, t)
        if width == 0.0:
            return
        height = float_at_time(self.height, t)
        if height == 0.0:
            return

        x0 = 0.0
        y0 = 0.0

        x1 = x0 + width
        y1 = y0 + height

        with _xform_context(ctx, self.local_xform(t)):
            if not self.fill_color.is_transparent():
                ctx.set_line_width(float_at_time(self.border_width, t))
                ctx.move_to(x0, y0)
                ctx.line_to(x0, y1)
                ctx.line_to(x1, y1)
                ctx.line_to(x1, y0)
                ctx.close_path()
                ctx.set_source_rgba(*self.fill_color.tuple(t, alpha_multiplier=alpha))
                ctx.clip()
                ctx.paint()
                ctx.reset_clip()

            if not self.line_color.is_transparent():
                sample_times = np.linspace(self.min_time, self.max_time, self.steps + 1)

                sample_values = [self._tvf(time) for time in sample_times]

                if self.min_value is None or self.max_value is None:
                    m0 = min(sample_values)
                    m1 = max(sample_values)

                if self.min_value is None:
                    min_value = m0 - 0.25 * (m1 - m0)
                else:
                    min_value = self.min_value

                if self.max_value is None:
                    max_value = m1 + 0.25 * (m1 - m0)
                else:
                    max_value = self.max_value

                ctx.set_line_width(float_at_time(self.border_width, t))
                ctx.set_source_rgba(*self.line_color.tuple(t, alpha_multiplier=alpha))

                for time, value in zip(sample_times, sample_values):
                    point_x = x0 + width * (
                            (time - self.min_time) / (self.max_time - self.min_time)
                    )
                    point_y = y0 + height - height * (
                            (value - min_value) / (max_value - min_value)
                    )
                    ctx.line_to(point_x, point_y)

                ctx.stroke()

            if not self.border_color.is_transparent():
                ctx.set_line_width(float_at_time(self.border_width, t))
                ctx.move_to(x0, y0)
                ctx.line_to(x0, y1)
                ctx.line_to(x1, y1)
                ctx.line_to(x1, y0)
                ctx.close_path()
                ctx.set_source_rgba(*self.border_color.tuple(t, alpha_multiplier=alpha))
                ctx.stroke()

                if self.time_ticks is not None:
                    for time_tick in self.time_ticks:
                        tick_x = x0 + width * (
                            (time_tick - self.min_time) / (self.max_time - self.min_time)
                        )
                        ctx.move_to(tick_x, y1)
                        ctx.line_to(tick_x, y1 + 10)
                        ctx.stroke()

                        tick_label = "{:.1f}".format(time_tick)

                        lines = walk_text(
                            ctx, tick_label, tick_x - 20, y1 + 15, 40, 12, 1.2,
                            TextJustification.CENTER
                        )

                        for line_x, line_y, line in lines:
                            if line is not None:
                                ctx.move_to(line_x, line_y)
                                ctx.show_text(line)

                if self.value_ticks is not None:
                    for value_tick in self.value_ticks:
                        tick_y = y0 + height - height * (
                                (value_tick - min_value) / (max_value - min_value)
                        )
                        ctx.move_to(x0, tick_y)
                        ctx.line_to(x0 - 10, tick_y)
                        ctx.stroke()

                        tick_label = "{:.1f}".format(value_tick)

                        lines = walk_text(
                            ctx, tick_label, x0 - 100, tick_y - 10.5, 85, 12, 1.2,
                            TextJustification.RIGHT
                        )

                        for line_x, line_y, line in lines:
                            if line is not None:
                                ctx.move_to(line_x, line_y)
                                ctx.show_text(line)

                if self.title is not None:
                    title_lines = walk_text(ctx, self.title, x0, y0 - 24, width, 14, 1.2,
                                            TextJustification.CENTER)

                    for line_x, line_y, line in title_lines:
                        if line is not None:
                            ctx.move_to(line_x, line_y)
                            ctx.show_text(line)
