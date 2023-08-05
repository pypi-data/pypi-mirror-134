"""
The TVX package is designed to model values that change over time.
It was created to power the :py:mod:`~gewel` package for creating
animations with simple scripts.

A time-varying quantity is--quite simply--alpha value that changes over
time. For example, the ``x`` coordinate of an object that moves
horizontally across the screen is alpha time-varying quantity. Using the
TVX package, this `x` coordinate can be represented by alpha time-varying
floating-point value of the class :py:class:`~pytvf.Tvf`.
"""

import os

from gewel._timekeeper import TimekeeperProtocol, TimekeeperMixin


class EnvPurePyException(Exception):
    pass


try:
    pure_py = os.environ.get('TVX_PURE_PYTHON', False)

    if pure_py:
        raise EnvPurePyException()

    from ctvx import (
        Tvb, Tvf,
        constant,
        cut,
        if_then_else,
        once,
        ramp,
        sample,
        time,

        min,
        max,

        sqrt,
        sin, cos, tan,
        asin, acos, atan,
        sinh, cosh, tanh,
        asinh, acosh, atanh,
    )

    tvx_is_ctvx = True

except (ImportError, EnvPurePyException):

    from pytvx import (
        PyTvb, PyTvf,
        constant,
        if_then_else,
        cut,
        once,
        ramp,
        sample,
        time,

        _min,
        _max,

        sqrt,
        sin, cos, tan,
        asin, acos, atan,
        sinh, cosh, tanh,
        asinh, acosh, atanh,
    )

    Tvb = PyTvb
    Tvf = PyTvf

    min = _min
    max = _max

    tvx_is_ctvx = False


from .types import (
    BoolOrTVB,
    FloatOrTVF,
)


class Tvd(dict, TimekeeperMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._time = 0.0

    @property
    def time(self) -> float:
        return self._time

    def set_time(self, t: float):
        self._time = t

    def get_at(self, k: str, t: float):
        val = super().__getitem__(k)
        if isinstance(val, (Tvf, Tvb, Tvd)):
            return val(t)
        else:
            return val

    def at(self, t: float):
        return {k: self.get_at(k, t) for k in self.keys()}

    def __call__(self, t: float):
        return self.at(t)

    class ItemRef():
        def __init__(self, tvd: 'Tvd', k: str):
            self._tvd = tvd
            self._k = k

        def __call__(self, t: float):
            return self._tvd.get_at(self._k, t)

        def __getattr__(self, attr):
            val = getattr(super(Tvd, self._tvd).get(self._k), attr)
            return val

    def __getitem__(self, k: str):
        if k not in self:
            raise KeyError(f"key '{k}' not present.")
        return Tvd.ItemRef(self, k)

    def cut_item_to(self, k: str, after: FloatOrTVF):
        self[k] = cut(super().__getitem__(k), self.time, after)

    def ramp_item_to(
            self: TimekeeperProtocol,
            k: str,
            to: float,
            duration: float,
            update_time: bool = True
    ):
        frm = super().__getitem__(k)
        if isinstance(frm, Tvf):
            frm_val = frm(self.time)
        else:
            frm_val = frm
        rmp = ramp(frm_val, to, self.time, duration)
        ct = cut(frm, self.time, rmp)
        super().__setitem__(k, ct)
        self._manage_time(duration, update_time)


def float_at_time(x: FloatOrTVF, t: float):
    if isinstance(x, Tvf):
        return x(t)
    else:
        return x
