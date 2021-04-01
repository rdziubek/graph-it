from point import Point


class Rectangle:
    """
    Holds the state of a rectangle that is being constructed based on its second anchor point
    as well as its static perimeter of 36 units.
    """
    BASE_PERIMETER = 36

    def __init__(self, second_anchor: Point = Point()):
        """
        Initialise the rectangle.
        :param second_anchor: The context for laying out rectangle's b upper right point.
        """
        self.a = Point(0, 0)
        self._b = self._initialise_with_argument(second_anchor)

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        self._b = self._initialise_with_argument(value)

    def _initialise_with_argument(self, point):
        return Point(point.x,
                     self._calculate_matching_height(abs(point.x - self.a.x)))

    def _calculate_matching_height(self, width):
        return (self.BASE_PERIMETER - 2 * width) / 2

    def get_width(self):
        return abs(self._b.x - self.a.x)

    def get_height(self):
        return abs(self._b.y - self.a.y)

    def get_area(self):
        return self.get_width() * self.get_height()

    def to_string(self):
        return f'anchor: {self._b.to_string()}, area: {self.get_area()}, ' \
               f'width: {self.get_width()}, height: {self.get_height()}'
