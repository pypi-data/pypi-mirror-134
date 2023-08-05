from typing import Optional, Tuple, Union
import numpy as np

import tvx
from tvx import Tvf, ramp, sample


def path(
        x0: float, y0: float,
        x1: float, y1: float,
        start: float,
        duration: float,
) -> Tuple[Tvf, Tvf]:

    t = ramp(x0=start, width=duration)

    x = x0 * (1 - t) + x1 * t
    y = y0 * (1 - t) + y1 * t

    return x, y


def quadratic_path(
        x0: float, y0: float,
        x1: float, y1: float,
        x2: float, y2: float,
        start: float,
        duration: float,
) -> Tuple[Tvf, Tvf]:

    t = ramp(x0=start, width=duration)

    x = x0 * (1 - t) * (1 - t) + 2 * (1 - t) * t * x1 + t * t * x2
    y = y0 * (1 - t) * (1 - t) + 2 * (1 - t) * t * y1 + t * t * y2

    return x, y


def bezier_path(
        x0: float, y0: float,
        x1: float, y1: float,
        x2: float, y2: float,
        x3: float, y3: float,
        start: float,
        duration: float,
) -> Tuple[Tvf, Tvf]:

    t = ramp(x0=start, width=duration)

    x = x0 * pow(1 - t, 3) + \
        x1 * 3 * pow(1 - t, 2) * t + \
        x2 * 3 * (1 - t) * pow(t, 2) + \
        x3 * pow(t, 3)
    y = y0 * pow(1 - t, 3) + \
        y1 * 3 * pow(1 - t, 2) * t + \
        y2 * 3 * (1 - t) * pow(t, 2) + \
        y3 * pow(t, 3)

    return x, y


def sine_wave(frequency: float, amplitude: tvx.FloatOrTVF = 1.0, phase: float = 0.0):
    return amplitude * tvx.sin(frequency * (2 * np.pi) * tvx.time() + phase)


def format_time(t: float, show_hours: Union[bool, str] = 'maybe') -> str:
    seconds, milliseconds = divmod(t, 1)
    milliseconds = int(round(1000 * milliseconds))
    seconds = int(seconds)
    minutes, seconds = divmod(seconds, 60)
    if (show_hours == 'maybe' and minutes >= 60) or (show_hours is True):
        hours, minutes = divmod(minutes, 60)
        hours = hours % 100
        return "{:02d}:{:02d}:{:02d}.{:03d}".format(hours, minutes, seconds, milliseconds)
    else:
        minutes = minutes % 100
        return "{:02d}:{:02d}.{:03d}".format(minutes, seconds, milliseconds)


def lin_space_sample(x: Tvf, start: float, stop: Union[float, int], num: Optional[int] = None):
    return sample(x, [float(x) for x in np.linspace(start, stop, num)])


def a_range_sample(x: Tvf, start: Optional[int] = None, *args, **kwargs):
    return sample(x, [float(x) for x in np.arange(start, *args, **kwargs)])
