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
        self.__width = value
    @height.setter
    def height(self, height):
        """setter for height"""
        self.__height = height
    @x.setter
    def x(self, x):
        """setter for x"""
        self.__x = x
    @y.setter
    def y(self, y):
        """setter for y"""
        self.__y = y

