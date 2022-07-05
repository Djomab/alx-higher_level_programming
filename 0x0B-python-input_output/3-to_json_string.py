#!/usr/bin/python3

"""Contains function that returns JSON representation of an object"""
import json


def to_json_string(my_obj):
    """Return JSON rep of my_obj
    Args:
        my_obj: an object
    Return:
        JSON rep of my_obj
    """
    return json.dumps(my_obj)
