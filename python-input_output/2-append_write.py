#!/usr/bin/python3
"""Append write module."""


def append_write(filename="", text=""):
    """Append a string to a text file (UTF8) and return characters added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
