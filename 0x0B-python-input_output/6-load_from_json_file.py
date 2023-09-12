#!/usr/bin/python3
"""
A function that reads ".JSON file" and converts to types of python
"""


import json


def load_from_json_file(filename):
    """
    Reads a .JSON file and converts its content (JSON) to python types
    Args:
      - filename: path
    """

    with open(filename, mode="r", encoding="utf-8") as _file:
        return (json.loads(_file.read()))
