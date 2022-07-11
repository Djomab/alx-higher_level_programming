#!/usr/bin/python3
"""Square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Return size of square"""
        return self.width

    @size.setter
    def size(self, val):
        """ set width and height to same value """
        self.width = val
        self.height = val

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                  self.size))
