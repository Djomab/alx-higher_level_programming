#!/usr/bin/python3
""" Square class """


class Square:
    """ Define a square """
    def __init__(self, size=0, position=(0, 0)):
        """
        Constructeur
        Args:
            size(int): size of square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """get square size"""
        return (self.__size)

    def position(self):
        """get square position"""
        return (self.__position)

    @size.setter
    def size(self, value):
        """set square size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self, value):
        """set square position"""
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        for item in value:
            if not isinstance(item, int) or item < 0:
                raise TypeError("position must be a tuple of"
                                + "2 positive integers")
        self.__size = value

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        i = 0
        j = 0
        if self.__size == 0:
            print('')
        else:
            for i in range(self.__position[1]):
                print('')

            for i in range(self.size):
                print(' ' * self.__position[0] + '#' * self.size)
