#!/usr/bin/python3
"""Base module"""


from fileinput import filename
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__+".json"
        with open(filename, 'w') as jf:
            if list_objs is None or not list_objs:
                jf.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jf.write(Base.to_json_string(list_dicts))
