#!/usr/bin/python3
"""This program validate if the obj is the same with other class
"""


def is_same_class(obj, a_class):
    """This function validate if obj is the same class of a_clas
    """
    return type(obj) is a_class
