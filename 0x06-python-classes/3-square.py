#!/usr/bin/python3
"""
Module: 2-square.py
this module defines a class Square which represents a square.
"""


class Square:
    """
    Defines a square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance.
        Args:
            size (int): The size of the square. Default value is 0.
        Raises:
            TypeError: If `size` is not an integer.
            ValueError: If `size` is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Computes the area of the square.
        Returns:
            The area of the square.
        """
        return self.__size ** 2
