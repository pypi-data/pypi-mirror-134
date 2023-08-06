from __future__ import annotations
from abc import ABC, abstractmethod
from enum import IntEnum, unique
from typing import List, Optional, Union

import numpy as np

from ..common.config import Config
from ..math.matrix import Matrix
from .geom_algo import GeomAlgo2D


class Shape(ABC):
    @unique
    class Type(IntEnum):
        BASE: int = -1
        Point: int = 0
        Polygon: int = 1
        Circle: int = 2
        Ellipse: int = 3
        Capsule: int = 4
        Edge: int = 5
        Curve: int = 6
        Sector: int = 7

    def __init__(self):
        self._type: Shape.Type = Shape.Type.BASE

    @property
    def type(self) -> Shape.Type:
        return self._type

    @type.setter
    def type(self, val: Shape.Type) -> None:
        self._type = val

    @abstractmethod
    def scale(self, factor: float) -> None:
        raise NotImplementedError

    @abstractmethod
    def contains(self, point: Matrix) -> bool:
        raise NotImplementedError

    @abstractmethod
    def center(self) -> Matrix:
        raise NotImplementedError


class ShapePrimitive():
    '''Basic Shape Description Primitive.
       Including vertices/position/angle of shape
    '''
    def __init__(self):
        self._shape: Optional[Union[Point, Polygon, Rectangle, Circle, Ellipse,
                                    Edge, Curve, Capsule, Sector]] = None
        self._xform: Matrix = Matrix([0.0, 0.0], 'vec')
        self._rot: float = 0.0

    def translate(self, src: Matrix) -> Matrix:
        assert src.shape == (2, 1)
        return Matrix.rotate_mat(self._rot) * src + self._xform


class Point(Shape):
    def __init__(self):
        super().__init__()
        self.type = self.Type.Point
        self._pos: Matrix = Matrix([0.0, 0.0], 'vec')

    @property
    def pos(self) -> Matrix:
        return self._pos

    @pos.setter
    def pos(self, pos: Matrix) -> None:
        self._pos = pos

    def scale(self, factor: float) -> None:
        self._pos *= factor

    def contains(self, point: Matrix) -> bool:
        return self._pos == point

    def center(self) -> Matrix:
        return self._pos


class Polygon(Shape):
    '''Convex polygon, not concve
    '''
    def __init__(self):
        super().__init__()
        self.type = self.Type.Polygon
        self._vertices: List[Matrix] = []

    @property
    def vertices(self) -> List[Matrix]:
        return self._vertices

    @vertices.setter
    def vertices(self, vertices: List[Matrix]) -> None:
        self._vertices = vertices
        self.update_vertices()

    def append(self, vertice: Matrix) -> None:
        raise AssertionError('dont use, otherwise make gjk algo fail! ')
        self._vertices.append(vertice)
        self.update_vertices()

    def scale(self, factor: float) -> None:
        assert len(self._vertices) > 0
        self._vertices = [v * factor for v in self._vertices]

    def contains(self, point: Matrix) -> bool:
        assert len(self._vertices) > 2

        vert_len: int = len(self._vertices)
        for i in range(vert_len - 1):
            p1: Matrix = self._vertices[i]
            p2: Matrix = self._vertices[i + 1]
            ref: Matrix = self._vertices[
                1] if i + 2 == vert_len else self._vertices[i + 2]
            # NOTE: why [1]? according to the vertices list type,
            # shape need to be closed
            if not GeomAlgo2D.is_point_on_same_side(p1, p2, ref, point):
                return False

        return True

    def center(self) -> Matrix:
        return GeomAlgo2D.calc_mass_center(self._vertices)

    def update_vertices(self) -> None:
        center_point: Matrix = self.center()
        self._vertices = [v - center_point for v in self._vertices]


class Rectangle(Polygon):
    def __init__(self, width: float = 0.0, height: float = 0.0):
        super().__init__()
        self.set_value(width, height)

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, width: float) -> None:
        self._width: float = width
        self.calc_vertices()

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, height: float) -> None:
        self._height: float = height
        self.calc_vertices()

    @property
    def vertices(self) -> List[Matrix]:
        return self._vertices

    @vertices.setter
    def vertices(self, vert: List[Matrix]) -> None:
        self._vertices = vert

    # NOTE: use _var to set val, because property 'width'
    # and 'height' call 'calc_vertices' will use _var in init
    def set_value(self, width: float, height: float) -> None:
        self._width = width
        self._height = height
        self.calc_vertices()

    def scale(self, factor: float) -> None:
        self._width *= factor
        self._height *= factor
        self.calc_vertices()

    @staticmethod
    def contain_helper(val: float, ref: float) -> bool:
        return -ref * 0.5 < val < ref * 0.5

    def contains(self, point: Matrix) -> bool:
        return self.contain_helper(point.x,
                                   self._width) and self.contain_helper(
                                       point.y, self._height)

    def calc_vertices(self) -> None:
        self._vertices: List[Matrix] = []
        self._vertices.append(
            Matrix([-self._width * 0.5, self._height * 0.5], 'vec'))
        self._vertices.append(
            Matrix([-self._width * 0.5, -self._height * 0.5], 'vec'))
        self._vertices.append(
            Matrix([self._width * 0.5, -self._height * 0.5], 'vec'))
        self._vertices.append(
            Matrix([self._width * 0.5, self._height * 0.5], 'vec'))
        self._vertices.append(
            Matrix([-self._width * 0.5, self._height * 0.5], 'vec'))


class Circle(Shape):
    def __init__(self, radius: float = 0.0):
        super().__init__()
        self.type = self.Type.Circle
        self.radius = radius

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, radius: float) -> None:
        self._radius: float = radius

    def scale(self, factor: float) -> None:
        self._radius *= factor

    def contains(self, point: Matrix) -> bool:
        return point.len_square() < self._radius * self._radius

    def center(self) -> Matrix:
        return Matrix([0.0, 0.0], 'vec')


class Ellipse(Shape):
    def __init__(self, width: float = 0.0, height: float = 0.0):
        super().__init__()
        self.type = self.Type.Ellipse
        self.set_value(width, height)

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, width: float) -> None:
        self._width: float = width

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, height: float) -> None:
        self._height: float = height

    def set_value(self, width: float, height: float) -> None:
        self._width = width
        self._height = height

    def scale(self, factor: float) -> None:
        self._width *= factor
        self._height *= factor

    def contains(self, point: Matrix) -> bool:
        return False

    def center(self) -> Matrix:
        return Matrix([0.0, 0.0], 'vec')

    def A(self) -> float:
        return self._width / 2.0

    def B(self) -> float:
        return self._height / 2.0

    def C(self) -> float:
        va = self.A()
        vb = self.B()
        return np.sqrt(va * va - vb * vb)


class Edge(Shape):
    def __init__(self):
        super().__init__()
        self.type = self.Type.Edge
        # set (1.0, 1.0) just for init calc the normal vec correctly
        # if both are (0.0, 0.0), can lead div zero error
        self.set_value(Matrix([1.0, 1.0], 'vec'), Matrix([0.0, 0.0], 'vec'))

    @property
    def start(self) -> Matrix:
        return self._start

    @start.setter
    def start(self, point: Matrix) -> None:
        self._start: Matrix = point
        self.update_normal()

    @property
    def end(self) -> Matrix:
        return self._end

    @end.setter
    def end(self, point: Matrix) -> None:
        self._end: Matrix = point
        self.update_normal()

    # the only method to init the edge value
    def set_value(self, start: Matrix, end: Matrix) -> None:
        self._start = start
        self._end = end
        self.update_normal()

    def update_normal(self) -> None:
        self._normal: Matrix = (self._end -
                                self._start).perpendicular().normal().negate()

    def scale(self, factor: float) -> None:
        self._start *= factor
        self._end *= factor

    def contains(self, point: Matrix) -> bool:
        return GeomAlgo2D.is_point_on_segment(self._start, self._end, point)

    def center(self) -> Matrix:
        return (self._start + self._end) / 2.0

    @property
    def normal(self) -> Matrix:
        return self._normal

    @normal.setter
    def normal(self, normal: Matrix) -> None:
        self._normal = normal


class Curve(Shape):
    def __init__(self):
        super().__init__()
        self.type = self.Type.Curve
        self.set_value(Matrix([0.0, 0.0], 'vec'), Matrix([0.0, 0.0], 'vec'),
                       Matrix([0.0, 0.0], 'vec'), Matrix([0.0, 0.0], 'vec'))

    @property
    def start(self) -> Matrix:
        return self._start

    @start.setter
    def start(self, point: Matrix) -> None:
        self._start: Matrix = point

    @property
    def ctrl1(self) -> Matrix:
        return self._ctrl1

    @ctrl1.setter
    def ctrl1(self, point: Matrix) -> None:
        self._ctrl1: Matrix = point

    @property
    def ctrl2(self) -> Matrix:
        return self._ctrl2

    @ctrl2.setter
    def ctrl2(self, point: Matrix) -> None:
        self._ctrl2: Matrix = point

    @property
    def end(self) -> Matrix:
        return self._end

    @end.setter
    def end(self, point: Matrix) -> None:
        self._end: Matrix = point

    def set_value(self, start: Matrix, ctrl1: Matrix, ctrl2: Matrix,
                  end: Matrix) -> None:
        self._start = start
        self._ctrl1 = ctrl1
        self._ctrl2 = ctrl2
        self._end = end

    def scale(self, factor: float) -> None:
        self._start *= factor
        self._ctrl1 *= factor
        self._ctrl2 *= factor
        self._end *= factor

    def contains(self, point: Matrix) -> bool:
        return False

    def center(self) -> Matrix:
        return Matrix([0.0, 0.0], 'vec')


class Capsule(Shape):
    def __init__(self, width: float = 0.0, height: float = 0.0):
        super().__init__()
        self.type = self.Type.Capsule
        self.set_value(width, height)

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, width: float) -> None:
        self._width: float = width

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, height: float) -> None:
        self._height: float = height

    def set_value(self, width: float, height: float) -> None:
        self._width = width
        self._height = height

    def calc_pos(self, sign: int = 1) -> List[float]:
        res: List[float] = []
        tmp: float = 0.0
        if self._width > self._height:
            tmp = self._height / 2.0
            res.append(-self._width / 2.0 + tmp)
            res.append(sign * tmp)
        else:
            tmp = self._width / 2.0
            res.append(-tmp)
            res.append(sign * (self._height / 2.0 - tmp))

        return res

    # NOTE: the capsule is made by 2 circle and 1 rectangle with
    # the radius go through the rectangle's width
    # so the top left is the circle's inscribe rectangle's top left point
    def top_left(self) -> Matrix:
        return Matrix(self.calc_pos(), 'vec')

    def bottom_left(self) -> Matrix:
        return Matrix(self.calc_pos(-1), 'vec')

    def top_right(self) -> Matrix:
        return -self.bottom_left()

    def bottom_right(self) -> Matrix:
        return -self.top_left()

    def box_vertices(self) -> List[Matrix]:
        vertices: List[Matrix] = []
        vertices.append(self.top_left())
        vertices.append(self.bottom_left())
        vertices.append(self.bottom_right())
        vertices.append(self.top_right())
        vertices.append(self.top_left())
        return vertices

    def scale(self, factor: float) -> None:
        self._width *= factor
        self._height *= factor

    @staticmethod
    def range_helper_x(p: Matrix, ref1: Matrix, ref2: Matrix,
                       idx: int) -> bool:
        if p._val[idx] - ref1._val[idx] <= Config.Epsilon and p._val[
                idx] - ref2._val[idx] >= Config.Epsilon:
            return True

        return False

    @staticmethod
    def range_helper_y(p: Matrix, idx: int, dis: float) -> bool:
        if p._val[idx] - dis <= Config.Epsilon and p._val[
                idx] + dis >= Config.Epsilon:
            return True

        return False

    @staticmethod
    def range_helper_val(p: Matrix, ref: Matrix, dis: float) -> bool:
        return (p - ref).len_square() - dis * dis <= Config.Epsilon

    def contains(self, point: Matrix) -> bool:
        anchor1: Matrix = Matrix([0.0, 0.0], 'vec')
        anchor2: Matrix = Matrix([0.0, 0.0], 'vec')
        x_len: float = 0.0
        y_len: float = 0.0

        if self._width >= self._height:
            y_len = self._height / 2.0
            x_len = self._width - self._height
            anchor1.set_value([x_len / 2.0, 0.0])
            anchor2.set_value([-x_len / 2.0, 0.0])
            if Capsule.range_helper_x(point, anchor1, anchor2,
                                      0) and Capsule.range_helper_y(
                                          point, 1, y_len):
                return True
        else:
            y_len = self._width / 2.0
            x_len = self._height - self._width
            anchor1.set_value([0.0, x_len / 2.0])
            anchor2.set_value([0.0, -x_len / 2.0])
            if Capsule.range_helper_x(point, anchor1, anchor2,
                                      1) and Capsule.range_helper_y(
                                          point, 0, y_len):
                return True

        # judge if the point in the arc part of the capsule
        if Capsule.range_helper_val(anchor1, point,
                                    y_len) or Capsule.range_helper_val(
                                        anchor2, point, y_len):
            return True

        return False

    def center(self):
        return Matrix([0.0, 0.0], 'vec')


class Sector(Shape):
    def __init__(self):
        super().__init__()
        self.type = self.Type.Sector
        self.set_value()

    def vertices(self) -> List[Matrix]:
        res: List[Matrix] = []
        res.append(Matrix([0.0, 0.0], 'vec'))
        res.append(
            Matrix.rotate_mat(self._start) * Matrix([self._radius, 0], 'vec'))
        res.append(
            Matrix.rotate_mat(self._start + self._span) *
            Matrix([self._radius, 0], 'vec'))
        res.append(Matrix([0.0, 0.0], 'vec'))
        return res

    @property
    def start(self) -> float:
        return self._start

    @start.setter
    def start(self, radian: float) -> None:
        self._start: float = radian

    @property
    def span(self) -> float:
        return self._span

    @span.setter
    def span(self, radian: float) -> None:
        self._span: float = radian

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, radius: float) -> None:
        self._radius: float = radius

    def set_value(self,
                  start: float = 0.0,
                  span: float = 0.0,
                  radius: float = 0.0) -> None:
        self._start = start
        self._span = span
        self._radius = radius

    def area(self) -> float:
        return self._span * self._radius * self._radius / 2.0

    def scale(self, factor: float) -> None:
        self._radius *= factor

    def contains(self, point: Matrix) -> bool:
        if np.isclose(point.x, 0):
            return 0 <= point.y <= self._radius
        else:
            theta: float = point.theta()
            ang_check1: bool = theta >= self._start
            ang_check2: bool = theta <= self._start + self._span
            len_check: bool = point.len_square() <= self._radius * self._radius
            return ang_check1 and ang_check2 and len_check

    def center(self) -> Matrix:
        vertices: List[Matrix] = self.vertices()
        point1: Matrix = vertices[1]
        point2: Matrix = vertices[2]
        normal: Matrix = (point1 + point2) / 2
        normal.normalize()

        point_len: float = (point1 - point2).len()
        rad_len: float = self._radius * self._span
        res: Matrix = normal * (2.0 * self._radius * point_len /
                                (3.0 * rad_len))

        return res
