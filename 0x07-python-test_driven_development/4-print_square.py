#!/usr/bin/python3


def print_square(size):
    """
    this function prints a square of size `size` using the char '#'.

    Args:
        size (int): The size length of the square.

    Raises:
        ValueError: If size is less than 0.
    """
    try:
        size = int(size)
    except ValueError:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
