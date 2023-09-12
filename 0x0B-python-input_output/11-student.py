#!/usr/bin/python3

"""this program writes a class Student"""


class Student:
    """Reps  a class Student"""
    def __init__(self, first_name, last_name, age):
        """init the attr of class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """fetches a dict rep of a Student instance"""
        if attrs is None:
            return self.__dict__

        else:
            d = {}
            for attr in attrs:
                if hasattr(self, attr):
                    d[attr] = getattr(self, attr)
            return d

    def reload_from_json(self, json):
        """replaces all attr of the Student instance"""
        for keys in json:
            setattr(self, keys, json[keys])
