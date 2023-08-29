#!/usr/bin/python3
"""my square module."""


class Square:
    """
    Represents a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.

        Raises:
            TypeError: If `size` is not an integer
            ValueError: If `size` is less than 0.
        """
        self.__size = size
        self.__position = position

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            A string representation of the square.
        """
        return self.my_print()

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
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
            The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: If `value` is not a tuple of 2 positive integers
        """
        if type(value) is not tuple or len(value) != 2 or \
                type(value[0]) is not int or type(value[1]) is not int or \
                value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            The area of the square.
        """
        return self.size ** 2

    def my_print(self):
        """
        Returns a string representing square with the character '#'.

        Returns:
            A string representation of the square.
        """
        result = ''
        if self.size == 0:
            return result

        for _ in range(self.position[1]):
            result += '\n'
        for _ in range(self.size):
            result += ' ' * self.position[0] + '#' * self.size + '\n'
        return result.rstrip()
