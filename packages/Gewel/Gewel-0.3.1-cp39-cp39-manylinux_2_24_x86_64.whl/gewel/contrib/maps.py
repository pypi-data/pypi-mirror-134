from abc import ABCMeta
from dataclasses import dataclass
from typing import Any, Dict, IO, Iterable, Optional, Union

import cairocffi as cairo
import geopandas as gpd
import numpy as np
from shapely.affinity import affine_transform, translate
from shapely.geometry import LineString, Polygon, MultiPolygon, Point
from shapely.geometry.base import BaseGeometry, BaseMultipartGeometry

import tvx
from gewel.color import BaseColor, BLACK, TRANSPARENT
from gewel.draw import (
    float_at_time, XYDrawable, BoundedMixin, _time_device_drawing, _xform_context,
    walk_text, TextJustification
)


def read_shapefile(path: Union[str, IO], crs: Optional[Any] = None) -> gpd.GeoDataFrame:
    gdf = gpd.read_file(path)
    if crs is not None:
        gdf.to_crs(crs, inplace=True)
    return gdf


@dataclass(init=False)
class ShapelyDrawable(XYDrawable, BoundedMixin, metaclass=ABCMeta):
    color: BaseColor = TRANSPARENT
    fill_color: BaseColor = TRANSPARENT
    marker_width: float = 8.0

    def __init__(
            self,
            geometry: Union[Polygon, MultiPolygon],
            color: BaseColor,
            fill_color: BaseColor = TRANSPARENT,
            line_width: tvx.FloatOrTVF = 1.0,
            text_color: Optional[BaseColor] = None,
            theta: tvx.FloatOrTVF = 0.0,
            centered: bool = True,
            z: tvx.FloatOrTVF = 0.0,
    ):
        x, y, max_x, max_y = geometry.bounds
        width, height = max_x - x, max_y - y
        if centered:
            x, y = x + width / 2, y + height / 2
        super().__init__(x=x, y=y, theta=theta, z=z)
        self._width = width
        self._height = height
        self.color = color
        self.fill_color = fill_color
        self.line_width = line_width
        if text_color is None:
            text_color = color
        self.text_color = text_color
        self.centered = centered

        if centered:
            self._geometry = translate(
                geometry,
                -self.x + self.width / 2,
                -self.y + self.height / 2
            )
        else:
            self._geometry = translate(geometry, -self.x, -self.y)

    @property
    def width(self) -> float:
        return self._width

    @property
    def height(self) -> float:
        return self._height

    def draw(self, ctx: cairo.Context, t: float) -> None:
        with _time_device_drawing():
            xform = self.local_xform(t)
            with _xform_context(ctx, xform):
                if not self.color.is_transparent() or not self.fill_color.is_transparent():
                    _draw_geometry(
                        ctx, t, self._geometry,
                        self.color, self.fill_color,
                        self.line_width, self.marker_width, self.alpha
                    )


def _draw_point(
        ctx: cairo.Context,
        t: float,
        point: Point,
        fill_color: BaseColor,
        marker_width: float,
        color: BaseColor,
        line_width: float,
        alpha: float
):
    if marker_width != 0.0:
        if not fill_color.is_transparent():
            ctx.set_source_rgba(*fill_color.tuple(t, alpha_multiplier=float_at_time(alpha, t)))
            ctx.arc(point.x, point.y, marker_width / 2, 0.0, 2 * np.pi)
            ctx.close_path()
            ctx.clip()
            ctx.paint()
            ctx.reset_clip()

        if not color.is_transparent():
            ctx.set_source_rgba(*color.tuple(t, alpha_multiplier=float_at_time(alpha, t)))
            ctx.arc(point.x, point.y, marker_width / 2, 0.0, 2 * np.pi)
            ctx.set_line_width(line_width)
            ctx.stroke()


def _draw_polygon(
        ctx: cairo.Context,
        t: float,
        polygon: Polygon,
        color: BaseColor,
        fill_color: BaseColor,
        line_width: float,
        alpha: float
):
    ctx.set_fill_rule(cairo.FILL_RULE_EVEN_ODD)
    ctx.set_line_width(line_width)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)

    exterior_points = polygon.exterior.coords

    for x, y in exterior_points:
        ctx.line_to(x, y)
    ctx.close_path()
    ctx.clip_preserve()

    for interior in polygon.interiors:
        interior_points = interior.coords

        for x, y in interior_points:
            ctx.line_to(x, y)
        ctx.close_path()

    ctx.clip()

    ctx.set_source_rgba(*fill_color.tuple(t, alpha_multiplier=float_at_time(alpha, t)))
    ctx.paint()
    ctx.reset_clip()

    if not color.is_transparent():
        ctx.set_source_rgba(*color.tuple(t, alpha_multiplier=float_at_time(alpha, t)))

        exterior_points = polygon.exterior.coords

        for x, y in exterior_points:
            ctx.line_to(x, y)
        ctx.stroke()

        for interior in polygon.interiors:
            interior_points = interior.coords

            for x, y in interior_points:
                ctx.line_to(x, y)
            ctx.stroke()


def _draw_line_string(
        ctx: cairo.Context,
        t: float,
        line_string: LineString,
        color: BaseColor,
        line_width: float,
        alpha: float
):
    if not color.is_transparent():
        ctx.set_source_rgba(*color.tuple(t, alpha_multiplier=float_at_time(alpha, t)))

        ctx.set_line_width(line_width)
        ctx.set_line_cap(cairo.LINE_CAP_ROUND)

        points = line_string.coords

        if len(points):
            ctx.move_to(*points[0])
            for x, y in points[1:]:
                ctx.line_to(x, y)

            ctx.stroke()


def _draw_geometry(
        ctx: cairo.Context,
        t: float,
        geometry: BaseGeometry,
        color: BaseColor,
        fill_color: BaseColor,
        line_width: float,
        marker_width: float,
        alpha: float,
):
    if isinstance(geometry, Point):
        _draw_point(ctx, t, geometry, fill_color, marker_width, color, line_width, alpha)
    elif isinstance(geometry, Polygon):
        _draw_polygon(ctx, t, geometry, color, fill_color, line_width, alpha)
    elif isinstance(geometry, LineString):
        _draw_line_string(ctx, t, geometry, color, line_width, alpha)
    elif isinstance(geometry, BaseMultipartGeometry):
        for g in geometry.geoms:
            _draw_geometry(ctx, t, g, color, fill_color, line_width, marker_width, alpha)
    else:
        raise ValueError("Unrecognized geometry type {:}".format(type(geometry)))


def _draw_geometry_label(
        ctx: cairo.Context,
        t: float,
        geometry: BaseGeometry,
        alpha: float,
        label: str,
        text_color: BaseColor,
        font_size: float,
        glow_color: Optional[BaseColor] = None,
        glow_width: float = 1.0,
):
    if label is not None:
        p = geometry.centroid
        lines = walk_text(
            ctx, label, p.x - 100, p.y, 200, font_size, 1.2,
            TextJustification.CENTER,
        )

        ctx.set_font_size(font_size)

        dy = -0.6 * font_size * (len(lines) + 1 - 1)

        for line_x, line_y, line in lines:
            if line is not None:
                if glow_color is not None and not glow_color.is_transparent() and glow_width != 1:
                    ctx.set_line_width(glow_width * 2)
                    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
                    ctx.set_source_rgba(*glow_color.tuple(t, alpha_multiplier=float_at_time(alpha, t)))
                    ctx.move_to(line_x, line_y + dy)
                    ctx.text_path(line)
                    ctx.stroke()

            ctx.set_source_rgba(*text_color.tuple(t, alpha_multiplier=float_at_time(alpha, t)))
            ctx.move_to(line_x, line_y + dy)
            ctx.show_text(line)


@dataclass(init=False)
class MapDrawable(XYDrawable, BoundedMixin):
    width: tvx.FloatOrTVF = 0.0
    height: tvx.FloatOrTVF = 0.0
    color: BaseColor = BLACK
    fill_color: BaseColor = TRANSPARENT
    line_width: tvx.FloatOrTVF = 1.0
    marker_width: float = 16.0
    text_color: BaseColor = BLACK
    font_size: float = 9
    highlight_line_width: tvx.FloatOrTVF = 5.0,
    centered: bool = True

    def _region_drawable(self, geometry: Union[Polygon, MultiPolygon], **kwargs) -> ShapelyDrawable:
        default_kwargs = {
            'line_width': self.line_width,
            'color': self.color,
            'fill_color': self.fill_color,
            'text_color': self.text_color,
        }
        all_kwargs = dict(**default_kwargs, **kwargs)

        if isinstance(geometry, (Polygon, MultiPolygon)):
            return ShapelyDrawable(geometry, **all_kwargs)
        else:
            raise ValueError(
                "Each geometry must either be a Polygon or BasePolygon; got a {:}".format(type(geometry))
            )

    def __init__(
            self,
            regions: Iterable[Dict[str, Any]],
            x: tvx.FloatOrTVF,
            y: tvx.FloatOrTVF,
            width: tvx.FloatOrTVF,
            height: tvx.FloatOrTVF,
            color: BaseColor = BLACK,
            fill_color: BaseColor = TRANSPARENT,
            line_width: tvx.FloatOrTVF = 1.0,
            marker_width: float = 16.0,
            text_color: Optional[BaseColor] = None,
            font_size: Optional[float] = None,
            highlight_line_width: tvx.FloatOrTVF = 5.0,
            map_base: Optional['MapDrawable'] = None,
            theta: tvx.FloatOrTVF = 0.0,
            centered: bool = True,
            z: tvx.FloatOrTVF = 0.0,
            alpha: tvx.FloatOrTVF = 1.0
    ):
        if centered:
            x = x + width / 2
            y = y + height / 2
        super().__init__(x, y, theta, z, alpha)
        self.width = width
        self.height = height
        self.color = color
        self.fill_color = fill_color
        self.line_width = line_width
        self.marker_width = marker_width
        if text_color is None:
            text_color = color
        self.text_color = text_color
        if font_size is None:
            font_size = 9
        self.font_size = font_size
        self.highlight_line_width = highlight_line_width
        if map_base is None:
            map_base = self
        self._map_base = map_base
        self.centered = centered

        self._regions = list(regions)

        self._regions.sort(key=lambda r: r.get('z', 0.0))

        bounds = [r['geometry'].bounds for r in self._regions]

        min_x = min([b[0] for b in bounds])
        min_y = min([b[1] for b in bounds])
        max_x = max([b[2] for b in bounds])
        max_y = max([b[3] for b in bounds])

        self._raw_width = max_x - min_x
        self._raw_height = max_y - min_y

        self._raw_x = min_x
        self._raw_y = min_y

        self._drawing_kwargs = {
            'line_width': self.line_width,
            'color': self.color,
            'fill_color': self.fill_color,
            'marker_width': self.marker_width,
            'alpha': self.alpha,
        }

        self._label_kwargs = {
            'alpha': self.alpha,
            'text_color': self.text_color,
            'font_size': self.font_size,
        }

    @property
    def raw_x(self):
        return self._raw_x

    @property
    def raw_y(self):
        return self._raw_y

    @property
    def raw_width(self):
        return self._raw_width

    @property
    def raw_height(self):
        return self._raw_height

    def draw(self, ctx: cairo.Context, t: float) -> None:
        xform = self.local_xform(t)
        region_xform_tuple = self._region_xform_tuple(t)
        with _xform_context(ctx, xform):
            for region in self._regions:
                draw_kwargs = dict(self._drawing_kwargs)

                transformed_region = dict(region)
                transformed_region['geometry'] = affine_transform(
                    region['geometry'], region_xform_tuple
                )

                draw_kwargs.update({
                    k: v for k, v in transformed_region.items()
                    if k not in [
                        'label', 'font_size', 'text_color',
                        'highlight_color', 'highlight_alpha', 'highlight_line_width',
                        'glow_color', 'glow_width',
                        'z',
                    ]
                })

                _draw_geometry(ctx, t, **draw_kwargs)

            # An optional highlight in a separate loop so it is
            # on top of all of the geometry and none of the
            # geometry of other regions can get drawn over it.
            for region in self._regions:
                if 'highlight_color' in region.keys():
                    draw_highlight_kwargs = dict()
                    draw_highlight_kwargs['geometry'] = affine_transform(
                        region['geometry'], region_xform_tuple
                    )
                    draw_highlight_kwargs['color'] = region['highlight_color']
                    draw_highlight_kwargs['fill_color'] = TRANSPARENT
                    draw_highlight_kwargs['line_width'] = region.get(
                        'highlight_line_width', self.highlight_line_width
                    )
                    draw_highlight_kwargs['marker_width'] = 0.0
                    draw_highlight_kwargs['alpha'] = region.get(
                        'highlight_alpha', self.alpha
                    )

                    _draw_geometry(ctx, t, **draw_highlight_kwargs)

            # We draw the label in a separate loop so it is
            # on top of all of the geometry and none of the
            # geometry of other regions can get drawn over it.
            for region in self._regions:
                if 'label' in region.keys():
                    draw_label_kwargs = dict(self._label_kwargs)

                    transformed_region = dict(region)
                    transformed_region['geometry'] = affine_transform(
                        region['geometry'], region_xform_tuple
                    )

                    draw_label_kwargs.update({
                        k: v for k, v in transformed_region.items()
                        if k not in [
                            'color', 'fill_color', 'line_width', 'marker_width',
                            'highlight_color', 'highlight_alpha', 'highlight_line_width',
                            'z',
                        ]
                    })

                    _draw_geometry_label(ctx, t, **draw_label_kwargs)

    def _region_xform_tuple(self, t: float):
        # So we have two libraries loaded, cairo and
        # shapely, both of which can do affine transforms.
        # shapely has the advantage that we can, in one
        # call, apply a transform to all the points in
        # a BaseGeometry. But cairo has the advantage that
        # we can multiply transform matrices together to
        # get a matrix that represents a series of
        # translations and rotations in a single matrix.
        # That's a key point of the power of affine
        # transformation. But shapely has no such notion.
        # It just uses tuples as the matrices and has
        # some helper methods to translate and rotate a
        # geometry.
        #
        # So, in an attempt to get the best of both worlds,
        # we construct a transform matrix using cairo, then
        # convert that into a tuple that shapely can use.
        # This lets us do the matrix construction once and
        # then apply it to each point of each geometry as
        # apposed to applying each individual sub-transform
        # (translation or rotation) to every point, which
        # results in a lot more multiplication and adding
        # overall.
        #
        # We construct the matrix here and then return it to
        # ``draw``, which applies it once to each geometry.
        width = float_at_time(self._map_base.width, t)
        height = float_at_time(self._map_base.height, t)

        # Move the raw center to the origin.
        translate_to_origin = cairo.Matrix(
            x0=-(self._map_base._raw_x + self._map_base._raw_width / 2),
            y0=-(self._map_base._raw_y + self._map_base._raw_height / 2)
        )

        # Flip vertically.
        flip = cairo.Matrix(xx=1.0, yy=-1.0)

        # Scale to the max size that fits in our boundary.
        scale_x = width / self._map_base._raw_width
        scale_y = height / self._map_base._raw_height
        scale_both = min(scale_x, scale_y)
        scale_to_max = cairo.Matrix(xx=scale_both, yy=scale_both)

        # Translate back in drawing coordinates.
        translate_back = cairo.Matrix(x0=width / 2, y0=height / 2)

        xform = translate_to_origin * flip * scale_to_max * translate_back

        xform_tuple = (xform.xx, xform.xy, xform.yx, xform.yy, xform.x0, xform.y0)

        return xform_tuple
