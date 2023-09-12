#!/usr/bin/python3
"""
this program writes a class Student
"""


class Student:
    """Reps a student."""

    def __init__(self, first_name, last_name, age):
        """Init a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dict rep of the Student instance.
        """
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__

        return {attr: getattr(self, attr) for attr in attrs
                if hasattr(self, attr)}
