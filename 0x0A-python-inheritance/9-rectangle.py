#!/usr/bin/python3

"""Rectangle class definition"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Reps Rectangle obj inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """Initializes Rectangle instance."""
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """Computes and return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self) -> str:
        """Return the string representation of the Rectangle."""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
