#!/usr/bin/python3

"""Defines a rectangle"""


class Rectangle():
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """
        Defines a rectangle

        Args:
            width: private attribute
            height: private attribute
        """
        self.__width = width
        self.__height = height
    
    @property
    def width(self):
        """Return width of rectangle"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """
        Setter of with
        Arg:
            value: value of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter of height
        Arg:
            value: value of height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value