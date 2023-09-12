#!/usr/bin/python3
"""
This program writes to a file, if the file doesn't exist,
it creates it
"""


def write_file(filename="", text=""):
    """
    Write to a file, if it doesn't exist, create the file
    Args:
      - filename: string
      - text: string
    """

    with open(filename, mode="w", encoding="utf-8") as _file:
        _file.write(text)

    return (len(text))
