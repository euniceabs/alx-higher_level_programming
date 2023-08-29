#!/usr/bin/python3
"""
Module: 4-square.py
This module defines a class Square that represents a square.
"""


class Square:
    """
    Represents a square.
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
        self.__size = 0
        self.size = size

    @property
    def size(self):
        """
        Fetches the size of the square.
        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.
        Args:
            value (int): The size of the square.
        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Computes the area of the square.
        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square in stdout with the character '#'.
        If the size is 0, it prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            square = [["#" for _ in range(self.__size)] for _ in
                      range(self.__size)]
            for row in square:
                print("".join(row))
