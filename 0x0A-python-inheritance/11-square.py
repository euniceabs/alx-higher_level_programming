#!/usr/bin/python3
"""
Defines a Square class
"""


PrevSquare = __import__('10-square').Square


class Square(PrevSquare):
    """
    sqaure class inherting from Rectangle
    """

    def __init__(self, size):
        """Initializes an improved Square"""
        super().__init__(size)

    def __str__(self):
        """Returns a string representation of Square"""
        return '[Square] {0:d}/{0:d}'.format(self.__size)
