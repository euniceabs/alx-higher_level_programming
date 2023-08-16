#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for key, value in a_dictionary.items():
        if isinstance(value, int):
            new_dictionary[key] = value * 2
        else:
            new_dictionary[key] = value
    return new_dictionary
