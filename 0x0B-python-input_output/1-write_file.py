#!/usr/bin/python3
"""
this module contains the write_file function
"""


def write_file(filename="", text=""):
    """writes a string to a text file and returns number of chars printed"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
