#!/usr/bin/python3
"""The rectangle class module"""

from models.base import Base


class Rectangle(Base):
    """ Repesents a rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """ set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """"retrieve the x value of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """ set the x value of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """"retrieve the y value of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """ set the y value of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the
        character #
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """String representation of the Rectangle instance.

        Returns:
        str: The string representation of the Rectangle instance.
        """

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        args_num = len(args)
        if args_num >= 1:
            self.id = args[0]
        if args_num >= 2:
            self.width = args[1]
        if args_num >= 3:
            self.height = args[2]
        if args_num >= 4:
            self.x = args[3]
        if args_num >= 5:
            self.y = args[4]

        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the Rectangle"""
        return {
            key: getattr(self, key)
            for key in ['id', 'width', 'height', 'x', 'y']
        }
