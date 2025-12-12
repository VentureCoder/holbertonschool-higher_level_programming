#!/usr/bin/python3
"""MyList module."""


class MyList(list):
    """Custom list class with sorted print method."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
