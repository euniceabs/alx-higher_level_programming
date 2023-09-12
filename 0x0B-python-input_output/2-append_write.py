#!/usr/bin/python3
"""
This program can append text in a file,
and then creates the file if it doesn't exist
"""


def append_write(filename="", text=""):
    """
    function that appends a text file
    and creates the file if doesn't exist
    """
    with open(filename, 'a', encoding='utf-8') as file:
        char_num = file.write(text)
    return char_num
