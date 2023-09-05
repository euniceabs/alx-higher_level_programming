#!/usr/bin/python3
""" this class defines a rectangle
"""


class Rectangle:
    """this class defines a rectangle."""

    def __init__(self, width=0, height=0):
        """this initializes a rectangle object with a
        given width and height."""
        self.__width = width
        self.__height = height

    def get_width(self):
        """this retrieves the width of the rectangle."""
        return self.__width

    def set_width(self, value):
        """this sets the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def get_height(self):
        """this function retrieve the height of the rectangle."""
        return self.__height

    def set_height(self, value):
        """helps set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    width = property(get_width, set_width)
    height = property(get_height, set_height)
