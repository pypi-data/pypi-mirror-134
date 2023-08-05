from abc import abstractmethod
from typing import Callable

import cairocffi as cairo

import tvx
from gewel.draw import Drawable


class TvDrawable(Drawable):
    def __init__(
            self,
            tvd_kwargs: tvx.Tvd,
    ):
        super().__init__()
        self._tvd_kwargs = tvd_kwargs
        self.wait_for(tvd_kwargs)

    @abstractmethod
    def drawable(self, **kwargs):
        raise NotImplementedError(str(type(self)) + " is abstract.")

    def draw(self, ctx: cairo.Context, t: float) -> None:
        kwargs = self._tvd_kwargs(t)
        drawable = self.drawable(**kwargs)
        drawable.draw(ctx, t)


def time_varying_drawable(func: Callable) -> Callable:
    """
    A decorator that decorates a function that returns
    a :py:class:`Drawable` and produces a function that
    takes a time-varying dictionary of class :py:class:`~tvx.Tvd`
    and used the values in it at the current time to
    produce a drawable.

    This is intended for very advanced use cases where neither the
    normal mechanics of :py:meth:`~gewel.XYDrawable.move_to`
    and similar functions nor motion linking (see
    :ref:`motion_linking_tracking_samples`,
    :ref:`partial_motion_linking_samples`, and
    :ref:`advanced_motion_linking`)
    are sufficient to create the desired effect. Note also that this
    approach is often much slower to render than those approaches.

    Parameters
    ----------
    func
        The function to be decorated.
    Returns
    -------
        A function that returns a drawable for the current
        time.
    """
    class _TvDrawable(TvDrawable):
        def drawable(self, **kwargs):
            return func(**kwargs)

    def _construct(tvd_kwargs: tvx.Tvd):
        return _TvDrawable(tvd_kwargs)

    return _construct
