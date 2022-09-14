#!/usr/bin/python3
"""A square class"""

class Square:
    """Represents a Square

    Atributes:
        __size(int): side of the square
    """
    def __init__(self, size = 0):
        """initializes a square with side of size

        Args:
            size(int): side of the squre

        Returns:
            None
        """
        self.size = size
    def area(self):
        """calculates area

        Returns: Area
        """
        return self.__size ** 2
    @property
    def size(self):
        """gets value of size

        Returns:
            Value of size
        """
        return self.__size
    @size.setter
    def size(self, value):
        """setter function method

        Args:
            value(int): length of the square

        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    def my_print(self):
        """Prints a square

        Returns: None
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for i in range(self.__size):
                print("#", end = "")
            print()
