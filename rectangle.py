import math

import numpy as np

from point import Point


class Rectangle:
    """
    Holds the state of a rectangle that is being constructed based on its second anchor point
    as well as its static perimeter of 36 units.
    """
    BASE_PERIMETER = 36
    TARGET_AREA = 81  # standard for a 9 by 9 rectangle (square) (optimal-valued)

    def __init__(self, width=0):
        """
        Initialise the rectangle.
        :param width: The context for laying out the rectangle.
        """
        self.a = Point(0, 0)
        self._b = self._initialise_with_argument(width)

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        self._b = self._initialise_with_argument(value)

    def _initialise_with_argument(self, width):
        return Point(self.a.x + width,
                     self.a.y + self._calculate_matching_height(width))

    def _calculate_matching_height(self, width):
        return self.TARGET_AREA / width if width != 0 else math.inf

    def get_width(self):
        return abs(self._b.x - self.a.x)

    def get_height(self):
        return abs(self._b.y - self.a.y)

    def get_area(self):
        return self.get_width() * self.get_height()

    def to_string(self):
        return f'anchor: {self._b.to_string()}, area: {self.get_area()}, ' \
               f'width: {self.get_width()}, height: {self.get_height()}'
