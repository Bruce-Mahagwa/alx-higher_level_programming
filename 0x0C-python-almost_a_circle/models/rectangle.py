#!/usr/bin/python3
"""
a Rectangle class that inherits from Base class
"""

from models.base import Base

class Rectangle(Base):
    """
    class Rectangle that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes the class"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
    @property
    def width(self):
        """getter for width"""
        return self.__width
    @property
    def height(self):
        """getter for height"""
        return self.__height
    @property
    def x(self):
        """getter for x"""
        return self.__x
    @property
    def y(self):
        """getter for y"""
        return self.__y
    @width.setter
    def width(self, value):
        """setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, height):
        """setter for height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """setter for x"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """setter for y"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
    def area(self):
        """gets the area of the rect

        Return: area"""
        return self.width * self.height
    def display(self):
        """displays the attr of the rect"""
        string = (" " * self.__x) + "#" * self.__width;
        for j in range(self.__height):
            print(string)
    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)
    def update(self, *args, **kwargs):
        count = 0
        if len(args):
            for i in args:
                count+=1
                if count == 0:
                    return
                elif count == 1:
                    self.id = args[0]
                elif count == 2:
                    self.__width = args[1]
                elif count == 3:
                    self.__height = args[2]
                elif count == 4:
                    self.__x = args[3]
                else:
                    self.__y = args[4]
        else:
            if kwargs is not None:
                for k in kwargs:
                    if k == "id":
                        self.id = kwargs[k]
                    elif k == "width":
                        self.__width = kwargs[k]
                    elif k == "height":
                        self.__height = kwargs[k]
                    elif k == "x":
                        self.__x = kwargs[k]
                    elif k == "y":
                        self.__y = kwargs[k]
    def to_dictionary(self):
        return {"id": self.id, "width": self.width, "height": self.height, "x": self.x, "y": self.y}
