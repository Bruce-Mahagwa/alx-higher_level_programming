#!/usr/bin/python3
"""
Represents calss BaseGeomwtry
"""


class BaseGeometry:
    """Creates a class BaseGeometry"""
    def area(self):
        """a public method area"""
        raise("area() is not implemented")
    def integer_validator(self, name, value):
        """a validator method for value"""
        if type(value) is not int:
            raise TypeError(name +  " must be an integer")
        if value <= 0 :
            raise ValueError(name + " must be greater than 0")
