#!/usr/bin/python3
"""
a class Square that inherits from Rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    a class Square that inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """initializes the class"""
        super().__init__(size, size, x, y, id)
        self.size = size
    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)
