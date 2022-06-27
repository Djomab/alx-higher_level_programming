#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """
    Defines a rectangle

    Args:
        width: private attribute
        height: private attribute
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
    
    @property
    def width(self):
        """
        Getter
        Return width of rectangle
        """
        return self.__width

    @property
    def height(self):
        """
        Getter
        Return height of rectangle
        """
        return self.__height
    
    @width.setter
    def width(self, value):
        """
        Setter of with
        Arg:
            value: value of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Setter of height
        Arg:
            value: value of height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
