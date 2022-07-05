#!/usr/bin/python3

"""Contain function that writes Object to text file"""
import json


def save_to_json_file(my_obj, filename):
    """Writes object to text file
    Args:
        my_obj: an object
        filename: name of the file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return json.dump(my_obj, f)
