#!/usr/bin/python3
"""
A function that reads files
"""


def read_file(filename=""):
    """
    This function reads a file and prints its contents
    """

    with open(filename, encoding="utf-8") as _file:
        print(_file.read(), end="")
