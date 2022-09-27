#!/usr/bin/python3
"""
read_file function that opens a fie
"""


def read_file(filename=""):
    """opens a file and prints its contents"""
    with open(filename, mode="r", encoding="utf-8") as f:
        read_line = f.read()
        for l in read_line:
            print(l, end="")
