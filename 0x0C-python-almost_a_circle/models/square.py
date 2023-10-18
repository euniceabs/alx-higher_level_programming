#!/usr/bin/python3
"""class Square that inherits from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ a class Sqaure"""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for Square class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of the Square instance.

        Returns:
        str: The string representation of the Square instance.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """retrieve the size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the size value of square"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args:
            attributes = ["id", "size", "x", "y"]
            for att, value in zip(attributes, args):
                setattr(self, att, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the Square"""
        return {
            key: getattr(self, key)
            for key in ['id', 'size', 'x', 'y']
        }
