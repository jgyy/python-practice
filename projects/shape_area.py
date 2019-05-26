"""
Shape Area and Perimeter Classes - Create an abstract class called Shape and then inherit from
it other shapes like diamond, rectangle, circle, triangle etc. Then have each class override
the area and perimeter functionality to handle each shape type.
"""
from abc import ABCMeta, abstractmethod
from math import pi, sqrt
import random


# noinspection PyCompatibility
class Shape(metaclass=ABCMeta):
    """Shape Class"""
    @abstractmethod
    def area(self):
        """area"""
        return 'area'

    @abstractmethod
    def perimeter(self):
        """perimeter"""
        return 'perimeter'


class Circle(Shape):
    """Circle Class"""
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """:return: radius"""
        return self._radius

    @property
    def area(self):
        """:return: area"""
        return pi * self._radius * self._radius

    @property
    def perimeter(self):
        """:return: perimeter"""
        return 2 * pi * self._radius


class Rectangle(Shape):
    """Rectangle Class"""
    def __init__(self, height, width):
        self._height = height
        self._width = width

    @property
    def height(self):
        """:return: height"""
        return self._height

    @property
    def width(self):
        """:return: width"""
        return self._width

    @property
    def area(self):
        """:return: area"""
        return self._width * self._height

    @property
    def perimeter(self):
        """:return: perimeter"""
        return 2 * (self._width + self._height)


class Triangle(Shape):
    """Triangle Class"""
    def __init__(self, side_a, side_b, side_c):
        self._side_a = side_a
        self._side_b = side_b
        self._side_c = side_c

    @property
    def get_sides(self):
        """
        :return: return list contain of three sides
        """
        return [self._side_a, self._side_b, self._side_c]

    @property
    def area(self):
        """
        http://en.wikipedia.org/wiki/Heron's_formula
        :return: based on Heron Formula
        """
        square = (self._side_a + self._side_b + self._side_c) / 2
        return sqrt(square * (square - self._side_a) *
                    (square - self._side_b) * (square - self._side_c))

    @property
    def perimeter(self):
        """:return: perimeter"""
        return self._side_a + self._side_b + self._side_c


if __name__ == '__main__':
    A = random.randint(1, 1111)
    B = random.randint(1, 1111)
    C = random.randint(1, 1111)
    D = random.randint(999, 1111)
    E = random.randint(999, 1111)
    F = random.randint(999, 1111)
    CI = Circle(A)
    RE = Rectangle(B, C)
    TR = Triangle(D, E, F)
    print("Circle Radius: ", CI.radius, " Area: ", CI.area, " Parameter: ", CI.perimeter)
    print("Rectangle Height: ", RE.height, " Width: ", RE.width,
          " Area: ", RE.area, " Parameter: ", RE.perimeter)
    print("Triangle Sides: ", TR.get_sides, " Area: ", TR.area, " Parameter: ", TR.perimeter)
