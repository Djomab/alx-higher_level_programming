#!/usr/bin/python3

"""Reading all agruments and adding them to list"""
import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    file = "add_item.json"
    args = sys.argv

    try:
        obj = load_from_json_file(file)
    except FileNotFoundError:
        obj = []
    obj.extend(args[1:])
    save_to_json_file(obj, file)
