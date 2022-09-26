#!/usr/bin/python3
"""class named BaseGeometry"""



class BaseGeometry:
    """A class with public instance methods area and integer_validator"""
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """validates that value is an integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:                                      
            raise ValueError("{:s} must be greater than 0".format(name))



"""
Represents the class Rectangle
"""



class Rectangle(BaseGeometry):
    """represents a rectangle"""
    def __init__(self, width, height):
        """instantiates the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
    def area(self):
        """returns area of the rect"""
        return self.__width * self.__height
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
