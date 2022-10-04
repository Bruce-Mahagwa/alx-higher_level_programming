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
        """str representation of attr"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)
    @property
    def size(self):
        """getter for size"""
        return self.width
    @size.setter
    def size(self, width):
        """setter for size"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.width = width
        self.height = width
    def update(self, *args, **kwargs):
        """method to update class attributes"""
        if len(args):
            count = 0
            for i in args:
                count += 1
                if count == 1:
                    self.id = args[0]
                elif count == 2:
                    self.size = args[1]
                elif count == 3:
                    self.x = args[2]
                elif count == 4:
                    self.y == args[3]
        else:
            if kwargs is not None:
                for k in kwargs:
                    if k == "id":
                        self.id = kwargs[k]
                    elif k == "size":
                        self.size = kwargs[k]
                    elif k == "x":
                        self.x = kwargs[k]
                    elif k == "y":
                        self.y = kwargs[k]
    def to_dictionary(self):
        """dictionary representation of attr"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}

