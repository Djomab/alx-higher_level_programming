#!/usr/bin/python3
"""
Print my name module
"""

def say_my_name(first_name, last_name=""):
    """
    function that prints My name is <first name> <last name>

    Args:
        first_name: first name
        last_name: last name optional with defaut value=""
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))