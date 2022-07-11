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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
        if not isinstance(val, (int, float)):
            raise TypeError("width must be an integer")
        elif val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @height.setter
    def height(self, val):
        """Set height val"""
        if not isinstance(val, (int, float)):
            raise TypeError("height must be an integer")
        elif val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @x.setter
    def x(self, val):
        """Set horizontal val"""
        if not isinstance(val, (int, float)):
            raise TypeError("x must be an integer")
        elif val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @y.setter
    def y(self, val):
        """Set vertical val"""
        if not isinstance(val, (int, float)):
            raise TypeError("y must be an integer")
        elif val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        """Returns the area value of the Rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """Prints in stdout the Rectangle with the character #"""
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for i in range(self.y):
            print()
        for row in range(self.__height):
            if row < (self.__height - 1):
                print((self.x * " ") + ("#" * self.__width))
            else:
                print((self.x * " ") + ("#" * self.__width))

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                        self.y,
                                                        self.__width,
                                                        self.__height))

    def update(self, *args, **kwargs):
        """ update attribute value """
        a = ["id", "width", "height", "x", "y"]
        if len(args) != 0 and args is not None:
            for i in range(len(args)):
                if i > len(a) - 1:
                    break
                setattr(self, a[i], args[i])
        else:
            for i in kwargs.keys():
                if i in a:
                    setattr(self, i, kwargs[i])

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        dictionnary = {}
        dictionnary['id'] = self.id
        dictionnary['width'] = self.width
        dictionnary['height'] = self.height
        dictionnary['x'] = self.x
        dictionnary['y'] = self.y
        return dictionnary


