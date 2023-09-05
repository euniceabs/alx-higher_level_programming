#!/usr/bin/python3
"""
Module for attribute prevention
"""


class LockedClass:
    """Class to prevent dynamic attributes creation"""

    __slots__ = ('first_name',)
