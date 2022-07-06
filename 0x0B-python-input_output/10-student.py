#!/usr/bin/python3
"""Student class module"""


class Student:
    """Defines student with attributes
    Attr:
        first_name: first name
        last_name: last name
        age: age of student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance
        with filter"""
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            new_dict = {}
            for element in attrs:
                if element in self.__dict__:
                    new_dict[element] = self.__dict__[element]
            return (new_dict)
        return (self.__dict__)
