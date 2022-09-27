#!/usr/bin/python3
"""
this module contains the append_write function
"""


def append_write(filename="", text=""):
    """appends text to a doc and returns number of chars added"""
    with open(filename, mode="a", encoding="utf-8") as f:
        write_line = f.write(text)
        return write_line
