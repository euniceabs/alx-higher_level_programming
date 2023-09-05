#!/usr/bin/python3


def matrix_divided(matrix, div):
    """
a funtion that divides matrix elements by a number and
rounds it to 2 decimal places.

    Args:
        matrix (list): List of lists representing a matrix.
        div (int or float): Number to divide the elements by.

    Returns:
        list: New matrix with rounded divided elements.

    Raises:
        TypeError: Invalid matrix or `div` is not a number.
        ZeroDivisionError: If `div` is zero.
    """
    if not isinstance(matrix, list) or \
            not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of ints/floats")
    row_lengths = set(len(row) for row in matrix)
    if len(row_lengths) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(element / div, 2) for element in row] for
                  row in matrix]
    return new_matrix
