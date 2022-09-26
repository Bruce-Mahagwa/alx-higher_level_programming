#!/usr/bin/python3
"""
Represents the class Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """represents a rectangle"""
    def __init__(self, width, height):
        """instantiates the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
    def area(self):
        """finds area"""
        return self.__width * self.__height
    def __str__(self):
        return "[Rectangle] " + <width>/<height>
