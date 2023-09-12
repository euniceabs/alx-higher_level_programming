#!/usr/bin/python3
"""This program takes the file "add_item.json", and adds the
parameters to the list inside this file.
"""
import sys
import json


def save_to_json_file(my_obj, filename):
    """
    this function writes an Obj to a text file, using a JSON rep
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """this function creates an obj from a “JSON file”"""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


try:
    my_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    my_list = []

for arg in sys.argv[1:]:
    my_list.append(arg)

save_to_json_file(my_list, "add_item.json")
