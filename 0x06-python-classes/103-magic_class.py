#!/usr/bin/python3
"""
Module: 103-magic_class.py
This module defines the MagicClass that performs calcs on a circle.
"""

import math


class MagicClass:
    """
    Represents a MagicClass that performs calcs on a circle.
    """

    def __init__(self, radius=0):
        """
        Initializes a MagicClass instance.
        Args:
            radius (int or float): The radius of the circle.
        Raises:
            TypeError: If `radius` is not a number.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calcs the area of the circle.
        Returns:
            The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calcs the circumference of the circle.
        Returns:
            The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
