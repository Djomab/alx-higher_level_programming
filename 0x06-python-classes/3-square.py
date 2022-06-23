#!/usr/bin/python3
""" Square class """


class Square:
    """ Define a square """
    def __init__(self, size=0):
        """
        Constructeur

        Args:
            size(int): size of square
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return (self.__size ** 2)
