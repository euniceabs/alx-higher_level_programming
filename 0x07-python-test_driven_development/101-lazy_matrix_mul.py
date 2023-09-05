#!/usr/bin/python3
"""this module defines a matrix mul function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """this function returns the mul of 2 matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    """

    return (np.matmul(m_a, m_b))
