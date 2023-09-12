#!/usr/bin/python3

"""a function that defines Rectangle class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Reps Rectangle obj which is inherited from Geometry."""

    def __init__(self, width, height):
        """Initialize rectangle instance"""
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
