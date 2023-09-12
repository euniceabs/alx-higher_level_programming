#!/usr/bin/python3

"""a class MyList that inherits from list"""


class MyList(list):
    """A subclass that inherits from a list"""
    def __init__(self):
        """initialize the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list(ascending sort)"""
        print(sorted(self))
