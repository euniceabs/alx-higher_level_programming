#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    copied_list = my_list.copy()

    if idx < 0 or idx >= len(copied_list):
        return copied_list

    copied_list[idx] = element
    return copied_list
