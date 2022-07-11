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

    def update(self, *args, **kwargs):
        """ update attribute value """
        a = ["id", "size", "x", "y"]
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
        """Returns the dictionary representation of a Square"""
        dictionnary = {}
        dictionnary['id'] = self.id
        dictionnary['size'] = self.size
        dictionnary['x'] = self.x
        dictionnary['y'] = self.y
        return dictionnary
