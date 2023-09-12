#!/usr/bin/python3
"""
A function that converts dict to JSON
"""


import json


def to_json_string(my_obj):
    """
    Converts a dict to JSON format
    Args:
     - my_obj: dict
    """

    return (json.dumps(my_obj))
