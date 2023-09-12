#!/usr/bin/python3
"""
This program converts JSON to dict
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Returns an object represented by a JSON string
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
