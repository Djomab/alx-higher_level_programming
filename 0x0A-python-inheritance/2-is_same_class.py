#!/usr/bin/python3
"""My module"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is an instance of a class
    Args:
        obj: object
        a_class: a class
    Return: True or False
    """
    return (type(obj) == a_class)
