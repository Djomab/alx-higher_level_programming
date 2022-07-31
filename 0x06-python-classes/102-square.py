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
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size ** 2)

    def __eq__(self, other):
        """Define the == comparision"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison"""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= compmarison"""
        return self.area() >= other.area()
