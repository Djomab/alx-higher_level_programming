#!/usr/bin/python3
"""Module that defines Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instance of Rectangle
        Args:
            width : width of rectangle
            height: height of rectangle
            x: x
            y: x
            id: id of class
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Return width of rectangle"""
        return self.__width

    @property
    def height(self):
        """Return height of rectangle"""
        return self.__height

    @property
    def x(self):
        """Return x of rectangle"""
        return self.__x

    @property
    def y(self):
        """Return y of rectangle"""
        return self.__y

    @width.setter
    def width(self, val):
        """Set width val"""
        self.__width = val

    @height.setter
    def height(self, val):
        """Set height val"""
        self.__height = val

    @x.setter
    def x(self, val):
        """Set horizontal val"""
        self.__x = val

    @y.setter
    def y(self, val):
        """Set vertical val"""
        self.__y = val
