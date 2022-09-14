#!/usr/bin/python3
"""Creates a Square class"""

class Square:
    """Represents a square"""
    def __init__(self, size = 0):
        """Initializes a square

        Args:
            size(int): Size of a square side

        Returns: None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
