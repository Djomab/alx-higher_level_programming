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
        self.size = size

    @property
    def size(self):
        """get square size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set square size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size ** 2)
