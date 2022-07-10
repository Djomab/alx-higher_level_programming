#!/usr/bin/python3
"""Base module"""


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Instanciation of Base
        Args:
            id: id of class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
