#!/usr/bin/python3
"""
containes a class called Base
"""


class Base:
    """
    a class called Base

    Attributes
    ----------
    __nb_objects: initialized to 0; a counter
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """
        Parameters
        ---------
        id: int
            identification which is unique
        """
        if id is not None:
            self.id = id
        else:
           Base.__nb_objects += 1
           self.id = Base.__nb_objects
