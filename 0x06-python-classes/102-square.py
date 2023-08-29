#!/usr/bin/python3
""" class Square that defines a square"""


class Square:
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self.validate_size(value)
        self._size = value

    @staticmethod
    def validate_size(value):
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.size ** 2

    def __eq__(self, other):
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __lt__(self, other):
        return not self.__ge__(other)

    def __le__(self, other):
        return not self.__gt__(other)
