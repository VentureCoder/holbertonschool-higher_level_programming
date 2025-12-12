#!/usr/bin/python3
"""Instance or inherited class check module."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is instance of or inherits from a_class."""
    return isinstance(obj, a_class)
