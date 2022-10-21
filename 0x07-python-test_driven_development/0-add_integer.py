#!/usr/bin/python3
"""
This is the add function
"""


def add_integer(a, b=98):
    """ Returns a + b """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
