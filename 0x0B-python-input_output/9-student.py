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

    def to_json(self):
        return self.__dict__
