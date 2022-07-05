#!/usr/bin/python3

"""Contains function that that returns an object represented by a JSON string"""
import json


def from_json_string(my_str):
    """Returns an object rep"""
    return json.loads(my_str)
