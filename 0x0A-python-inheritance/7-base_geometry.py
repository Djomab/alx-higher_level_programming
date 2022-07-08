#!/usr/bin/python3
"""A Geometry module"""


class BaseGeometry:
    """Empty class"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value
        Return True or False
        """
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
