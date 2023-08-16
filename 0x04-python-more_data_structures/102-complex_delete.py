#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    keys_to_delete = [key for key, value_ in a_dictionary.items()
                      if value_ == value]
    for key in keys_to_delete:
        a_dictionary.pop(key, None)
    return a_dictionary
