#!/usr/bin/python3
"""BaseGeometry module."""


class BaseGeometry:
    """Base geometry class."""
    def area(self):
        """Raise an exception for unimplemented area."""
        raise Exception("area() is not implemented")
