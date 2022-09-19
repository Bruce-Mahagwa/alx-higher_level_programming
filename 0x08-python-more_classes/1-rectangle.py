#!/usr/bin/python3
"""A Rectangle class"""
class Rectangle:
    """
        Defines a Rectangle class

        Attributes:
            __width(int): width of the rectangle
            __height(int): height of the rectangle
    """
    def __init__(self, width = 0, height = 0):
        """
            initializes a Rectangle

            Args: 
                width(int): side of the rectangle
                height(int): height of the rectangle
            Returns:
                None
        """
        self.width = width
        self.height = height
    @property
    def width(self):
        """getter for width"""
        return self.__width
    @width.setter
    def width(self, value):
        """
            setter for the width value

            Args:
                value(int): value to set the width
            Returns:
                None
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
    @property
    def height(self):
        """
            getter for height

            Returns:
                Value for height
        """
        return self.__height
    @height.setter
    def height(self, value):
        """
            setter for height

            Returns:
                None
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
