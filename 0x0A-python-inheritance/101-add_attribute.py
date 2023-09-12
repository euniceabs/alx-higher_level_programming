#!/usr/bin/python3
""" adds a new attribute to an object
"""


def add_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to an object if possible.
    Args:
        obj (object): The object to add attribute to.
        attr_name (str): The name of the attribute to add.
        attr_value: The value of the attribute.
    Raises:
        TypeError: If the object can't have new attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr_name, attr_value)
