#!/usr/bin/python3

"""Contain function that creates object from json file"""
import json


def load_from_json_file(filename):
    """Creates an Object from JSON file
    Args:
        filename: name of JSON file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
