#!/usr/bin/python3
"""The MyList class"""


class MyList(list):
    """initializes the class"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints the list"""
        print(sorted(self))
