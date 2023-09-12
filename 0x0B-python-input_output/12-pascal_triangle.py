#!/usr/bin/python3
"""
Pascal's triangle
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing
    the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangle = []
    for t in range(n):
        row = [1] * (t + 1)
        if t >= 2:
            for s in range(1, t):
                row[s] = triangle[t - 1][s - 1] + triangle[t - 1][s]
        triangle.append(row)

    return triangle
