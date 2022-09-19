#!/usr/bin/python3
"""A Rectangle class"""
class Rectangle:
    """
        Defines a Rectangle class

        Attributes:
            __width(int): width of the rectangle
            __height(int): height of the rectangle
    """
    number_of_instances = 0
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
        type(self).number_of_instances += 1
    def __del__(self):
        """Prints a message when an instance gets deleted"""
        print("Bye Rectangle . . .")
        type(self).number_of_instances -= 1
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
        elif value < 0:
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
    def area(self):
        """
            calculates area of the rectangle

            Returns: Area
        """
        return self.__width * self.__height
    def perimeter(self):
        """
            calculates perimeter of the rectangle

            Returns: Perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)
    def __str__(self):
        rec = ""
        if self.__width != 0 and self.__height != 0:
            rec += "\n".join("#" * self.__width for i in range(self.__height))
        return rec
    def __repr__(self):
        """turns the rectangle object into a string"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
