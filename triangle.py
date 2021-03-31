from point import Point
from polynomial import Polynomial


class Triangle:
    """
    Holds the state of a triangle constrained by points a, b and c.
    """

    def __init__(self, polynomial: Polynomial):
        """
        Initialise the triangle.
        :param polynomial: The context for laying out triangle's a and b points.
        """
        self.polynomial = polynomial
        self.a = Point(polynomial.argument, polynomial.value)
        self.b = Point(-polynomial.argument, polynomial.value)
        self.c = Point(0, -1 / 3)

    def _get_height(self):
        return abs(self.c.y) + self.polynomial.value

    def get_area(self):
        return 1 / 2 * (abs(self.a.x) + abs(self.b.x)) * self._get_height()

    def to_string(self):
        return f'Polynomial: {self.polynomial.to_string()}, B: {self.a.to_string()}, A: {self.b.to_string()}'
