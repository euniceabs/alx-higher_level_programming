#!/usr/bin/python3
"""a base geometry class definition
"""


class BaseGeometry:
    """
    Reps a Geometry obj
    """
    def area(self):
        """ computes the raise of a Geometry obj """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Check if value is a valid integer.
        Args:
            name (str): The name of the value.
            value (int): The value to be validated.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
