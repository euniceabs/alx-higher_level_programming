#!/usr/bin/python3

"""this program writes a class Student"""


class Student:
    """Represents Student"""
    def __init__(self, first_name, last_name, age):
        """init the attr of class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """fetches a dic rep of a Student instance"""
        return self.__dict__
