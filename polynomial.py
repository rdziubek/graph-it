import numpy as np


class Polynomial:
    def __init__(self, x):
        self.argument = x
        self._value = 9 / x ** 4

    @property
    def value(self):
        with np.errstate(divide='ignore', invalid='ignore'):
            return self._value

    @value.setter
    def value(self, value):
        with np.errstate(divide='ignore', invalid='ignore'):
            self._value = value

    def to_string(self):
        return vars(self)
