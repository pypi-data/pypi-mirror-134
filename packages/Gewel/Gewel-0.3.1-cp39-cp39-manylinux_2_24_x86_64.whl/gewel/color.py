"""
This module contains code related to colors.

Many of the objects gewel can render can be
rendered in a variety of colors. There are two
main classes of color that you are likely to
use, :py:class:`gewel.color.Color` and
:py:class:`gewel.color.ColorMap`,
both of which derive from the abstract base class
:py:class:`gewel.color.BaseColor`.

In many cases, you will not explicitly construct
objects of these classes, but rather use existing
color objects that are already defined for you. For
example:

.. code-block:: python

    import gewel.color as color

    my_color = color.RED
    my_other_color = color.DARK_GREY

    my_drawable.line_color = color.PURPLE

Of course, you can also create your own custom colors.
For example:

.. code-block:: python

    import gewel.color as color

    my_favorite_color = color.Color(0.6235, 0.8863, 0.7490)

    dark_shadow_color = color.Color(0.75, 0.75, 0.75, 0.25)

In the first case, ``my_favorite_color``, we
created a custom color by specifying the relative amounts of
red, green, and blue on a scale of 0.0 (none of the color) to 1.0
(the maximum amount).

In the second case, ``dark_shadow_color``, we
added an optional fourth
argument to specify the alpha of the color.
The alpha indicates how transparent the color
should be. 0.0 means completely transparent. 1.0 means
completely opaque. Leaving it out as we did
in ``my_favorite_color`` is equivalent to passing
in the default value of 1.0.
"""


from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Callable, Iterable, Optional, List, Tuple, Union

import colorcet as cc

import tvx
from gewel._timekeeper import TimekeeperMixin
from tvx import FloatOrTVF


class BaseColor(ABC):
    """
    The abstract base class for colors.
    """

    @abstractmethod
    def tuple(
            self, t: float, alpha_multiplier: tvx.FloatOrTVF = 1.0
    ) -> Tuple[float, float, float, float]:
        """
        Construct a `(red, green, blue, alpha)` tuple representing the color.
        The red, green, and blue
        components are determined by the color. The alpha component may be affected
        by the value of the alpha_multiplier parameter.

        Parameters
        ----------
        t
            The time for which we want the tuple.

        alpha_multiplier
            A multiplicative factor for the alpha. The value should be between
            0.0 and 1.0. It will be multiplied by the alpha of the color to
            produce the fourth element of the resulting tuple. Passing in 0.0
            will produce alpha transparent result (alpha = 0.0) while passing in
            the default value of 1.0 will leave the alpha of the color unchanged.

        Returns
        -------
        tuple
            A four element tuple, `(red, green, blue, alpha)` of color components for red,
            green, blue, and alpha (opacity). All are in the range [0.0, 1.0].
        """
        raise NotImplementedError(str(type(self)) + " is abstract.")

    @abstractmethod
    def is_transparent(self) -> bool:
        """
        Indicates whether the color is transparent or not, i.e. whether
        its alpha is certain to be zero. Checking this may be useful in
        checking whether something needs to be rendered or not. If the
        color it would be rendered is transparent then it does not.

        Returns
        -------
        bool
            True if the color is transparent. False otherwise.
        """
        raise NotImplementedError(str(type(self)) + " is abstract.")


@dataclass(init=False)
class Color(BaseColor):
    """
    A color with three components red, green, and blue representing
    the relative level or red, green, and blue respectively,
    and alpha fourth component alpha (alpha) representing opacity.
    All should be in the range [0.0, 1.0]. Note that these
    do not need to be fixed floating point values. They can
    also be time varying floats of type ~tvx.Tvf.

    An alpha value of 1.0 indicates opaque and 0.0 indicates
    transparent. Values in between are semi-transparent.

    Parameters
    ----------
    red
        Red color component.
    green
        Blue color component.
    blue
        Green color component.
    alpha
        Opacity. 0.0 means transparent. 1.0 means opaque.
        Values in between indicate partial transparency.
    """

    red: FloatOrTVF
    """Red color component."""
    green: FloatOrTVF
    """Green color component."""
    blue: FloatOrTVF
    """Blue color component."""
    alpha: FloatOrTVF
    """Opacity. 0.0 means transparent. 1.0 means opaque.
    Values in between indicate partial transparency.
    """

    def __init__(
            self,
            red: FloatOrTVF,
            green: FloatOrTVF,
            blue: FloatOrTVF,
            alpha: Optional[FloatOrTVF] = None
    ):
        if alpha is None:
            alpha = 1.0
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    def tuple(self, t: float, alpha_multiplier: tvx.FloatOrTVF = 1.0) -> Tuple[float, float, float, float]:
        am = float(alpha_multiplier)
        t = float(self.red), float(self.green), float(self.blue), float(self.alpha) * am
        return t

    def is_transparent(self) -> bool:
        return float(self.alpha) == 0.0

    _hex_digits = set('0123456789abcdefABCDEF')

    @classmethod
    def from_string(cls, hex_str: str) -> 'Color':
        """
        Construct  color from a hexadecimal string.

        The string
        should be of the form ``"#RRGGBB"`` or ``"#RRGGBBAA"`` where
        the characters ``RR`` are two hexadecimal digits representing
        the level of red in the color, ``BB`` is for blue, ``GG`` is for
        green, and ``AA`` is for the alpha component. Note that if
        ``AA`` is not present the color will be fully opaque (equivalent
        to an alpha of ``"FF"`` in hex.

        For example::

            red = Color.from_string('#FF0000') # implied alpha
            red_a = Color.from_string('#FF0000FF') # explicit alpha

            semi_transparent_red = Color.from_string('#FF00007F')

        produces three color objects. The first two are the exact same
        opaque red color. The third is also red, but it is semi-transparent,
        so when it is drawn, objects drawn under it will partially show
        through.

        There are many different color tables and pickers available to
        help you choose the hex strings for colors you might wish to
        use. The `Wikipedia page on web colors https://en.wikipedia.org/wiki/Web_colors`
        is a good place to start.

        Parameters
        ----------
        hex_str
            The hex string to parse out into a color.

        Returns
        -------
        Color
            A newly constructed object representing the color
            specified by the hex string.

        Raises
        ------
        ValueError
            if the string is not a proper hex string of the
            form ``"#RRGGBB"`` or ``"#RRGGBBAA"``.

        """
        # Make sure the format is good.
        good_string = True
        good_string = good_string and hex_str.startswith('#')
        good_string = good_string and len(hex_str) in [7, 9]

        for c in hex_str[1:]:
            good_string = good_string and c in Color._hex_digits
            if not good_string:
                break

        if not good_string:
            raise ValueError("Color string must be of the format '#RRGGBB' or '#RRGGBBAA' " +
                             "with components specified as hex digits. Received '{:s}'".format(hex_str))

        red = int(hex_str[1:3], 16) / 255.0
        green = int(hex_str[3:5], 16) / 255.0
        blue = int(hex_str[5:7], 16) / 255.0
        alpha = int(hex_str[7:9], 16) / 255.0 if len(hex_str) == 9 else 1.0

        return Color(red, green, blue, alpha)

    @classmethod
    def from_tuple(
            cls,
            tup: Union[
                Tuple[FloatOrTVF, FloatOrTVF, FloatOrTVF],
                Tuple[FloatOrTVF, FloatOrTVF, FloatOrTVF, FloatOrTVF]
            ]
    ) -> 'Color':
        return Color(*tup)

    def with_alpha(self, alpha: float) -> 'Color':
        return Color(self.red, self.green, self.blue, alpha)


TRANSPARENT = Color(0.0, 0.0, 0.0, 0.0)
"""
This is a completely transparent color. It is useful
when there are components of a drawable object that
we don't want to render. It is also commonly used as
a default color for portions of a drawable object.

For example, the class :py:class:`~gewel.draw.Box`
has both a color used to draw the border of the box
and a fill color to fill it with. Either can be transparent
as follows::

    from gewel.draw import Box
    from gewel.color import RED, TRANSPARENT

    # A red box that is not filled with any color.
    box1 = Box(color=RED, fill_color=TRANSPARENT)

    # A box filled with red but with no border.
    box2 = Box(color=TRANSPARENT, fill_color=RED)
"""

WHITE = Color(1.0, 1.0, 1.0)  #: White
LIGHT_GRAY = Color(0.75, 0.75, 0.75)  #: Light Gray
GRAY = Color(0.5, 0.5, 0.5)  #: Gray
DARK_GRAY = Color(0.25, 0.25, 0.25)  #: Dark Gray
BLACK = Color(0.0, 0.0, 0.0)  #: Black

RED = Color(1.0, 0.0, 0.0)  #: Red
GREEN = Color(0.0, 1.0, 0.0)  #: Green
BLUE = Color(0.0, 0.0, 1.0)  #: Blue

CYAN = Color(0.0, 1.0, 1.0)  #: Cyan
MAGENTA = Color(1.0, 0.0, 1.0)  #: Magenta
YELLOW = Color(1.0, 1.0, 0.0)  #: Yellow

MAROON = Color(0.5, 0.0, 0.0)  #: Maroon
DARK_GREEN = Color(0.0, 0.5, 0.0)  #: Dark Green
NAVY = Color(0.0, 0.0, 0.5)  #: Navy

TEAL = Color(0.0, 0.5, 0.5)  #: Teal
PURPLE = Color(0.5, 0.0, 0.5)  #: Purple
OLIVE = Color(0.5, 0.5, 0.0)  #: Olive

ORANGE = Color(1.0, 165.0 / 255.0, 0.0)  #: Orange

PINK = Color(1.0, 192.0 / 255.0, 203.0 / 255.0)  #: Pink

BACKGROUND = Color(240.0 / 255.0, 240.0 / 255.0, 240.0 / 255.0)
"""
This is a neutral color suitable for use as a background
in a variety of settings. It is a not quite bright white.
It is the default color for background objects of the class
:py:class:`~gewel.draw.Background`.
"""

# Follow matplotlib, which follows Vega and d3, which follow Tableau.
# https://matplotlib.org/stable/users/dflt_style_changes.html#colors-in-default-property-cycle
# https://github.com/vega/vega/wiki/Scales#scale-range-literals
# https://github.com/d3/d3-3.x-api-reference/blob/master/Ordinal-Scales.md#category10
CATEGORY_10 = [
    Color.from_string(s)
    for s in [
        '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
        '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'
    ]
]


def category10(index: int) -> Color:
    return CATEGORY_10[index % 10]


# d3: https://github.com/d3/d3-3.x-api-reference/blob/master/Ordinal-Scales.md#category20
CATEGORY_20 = [
    Color.from_string(s)
    for s in [
        '#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78', '#2ca02c',
        '#98df8a', '#d62728', '#ff9896', '#9467bd', '#c5b0d5',
        '#8c564b', '#c49c94', '#e377c2', '#f7b6d2', '#7f7f7f',
        '#c7c7c7', '#bcbd22', '#dbdb8d', '#17becf', '#9edae5'
    ]
]


def category20(index: int) -> Color:
    return CATEGORY_20[index % 20]


class ColorMap(BaseColor, TimekeeperMixin):
    """
    A color map is a color that is derived from other colors.

    Parameters
    ----------
    rgb_colors
        A list of colors that make up the map.
    position
        The location in the map whose color should be
        returned by :py:meth:`~ColorMap.tuple`.
    """
    def __init__(
            self,
            rgb_colors: Iterable[List[float]],
            position: Optional[FloatOrTVF] = None,
            min_position: float = 0.0,
            max_position: float = 1.0,
    ):
        self._rgb_colors = list(rgb_colors)
        if position is None:
            position = min_position
        self._position = position
        self._min_position = min_position
        self._max_position = max_position

        self._time = 0.0

    @property
    def r(self) -> 'ColorMap':
        return ColorMap(
            reversed(self._rgb_colors),
            self.position, self._min_position, self._max_position
        )

    @property
    def time(self) -> float:
        return self._time

    def set_time(self, time: float):
        self._time = time

    @property
    def position(self) -> FloatOrTVF:
        return self._position

    @position.setter
    def position(self, position: FloatOrTVF):
        self._position = position

    def tuple(self, t: float, alpha_multiplier: tvx.FloatOrTVF = 1.0) -> Tuple[float, float, float, float]:
        position = tvx.float_at_time(self._position, t)
        pos = ((position - self._min_position) /
               (self._max_position - self._min_position))
        pos = min(1.0, max(0.0, pos))

        n = len(self._rgb_colors)

        ii, rem = divmod(pos * (n - 1), 1)
        ii = int(ii)

        if rem == 0.0:
            rgb = self._rgb_colors[ii]
        else:
            rgb = [
                c0 * (1 - rem) + c1 * rem
                for c0, c1 in zip(self._rgb_colors[ii], self._rgb_colors[ii + 1])
            ]
        alpha = 1.0 if len(rgb) < 4 else rgb[3]
        return rgb[0], rgb[1], rgb[2], alpha * float(alpha_multiplier)

    def is_transparent(self) -> bool:
        return False

    def fade_to_position(self, position: FloatOrTVF, duration: float):
        self.ramp_attr_to('position', position, duration)

    @classmethod
    def from_colors(
            cls,
            colors: Iterable[Color],
            position: Optional[FloatOrTVF] = None,
            min_position: float = 0.0,
            max_position: float = 1.0,
    ) -> 'ColorMap':
        return ColorMap(
            [list(color.tuple(0)) for color in colors],
            position=position,
            min_position=min_position,
            max_position=max_position,
        )


def _reversible_color_map(func: Callable[[FloatOrTVF, float, float], ColorMap]):
    def reverse_color_func(
            position: FloatOrTVF = 0.0,
            min_position: float = 0.0,
            max_position: float = 1.0,
    ) -> ColorMap:
        return func(position, min_position, max_position).r

    func.r = reverse_color_func

    return func


def _color_map_factory(rgb_list: List[List[float]]):

    @_reversible_color_map
    def func(
            position: FloatOrTVF = 0.0,
            min_position: float = 0.0, max_position: float = 1.0
    ) -> ColorMap:
        return ColorMap(rgb_list, position, min_position, max_position)

    return func


# Slurp in all of the colors from cc.
for a in dir(cc):
    if not a.startswith('_'):
        v = getattr(cc, a)
        if isinstance(v, list) and isinstance(v[0], list) and len(v[0]) == 3:
            globals()[a] = _color_map_factory(v)
            for mapping in [cc.aliases, cc.aliases_v2, cc.mapping_flipped]:
                name = mapping.get(a, None)
                if name is not None:
                    globals()[name] = globals()[a]


# Like blues, but swapping blue and green.

def greens(
        position,
        min_position: float = 0.0,
        max_position: float = 1.0
):
    return ColorMap(
        [[row[0], row[2], row[1]] for row in cc.linear_blue_95_50_c20],
        position=position,
        min_position=min_position,
        max_position=max_position
    )
