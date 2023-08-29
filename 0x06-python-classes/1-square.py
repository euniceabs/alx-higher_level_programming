#!/usr/bin/python3
"""this is a class square that defines a square"""


class Square:
    """this class square represents a square"""

    def __init__(self, size=0):
        """this initializes a square
        Args:
            size (int): size of the square
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
