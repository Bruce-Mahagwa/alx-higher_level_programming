#!/usr/bin/python3
"""A Square class"""

class Square:
    """Represents a square

    Attributes:
       __size(int): side of a square

    Returns:
        None
    """
    def __init__(self, size = 0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        def area(self):
            """calculates the area

            Returns:
                Square area
            """
            return self.__size * self.__size
