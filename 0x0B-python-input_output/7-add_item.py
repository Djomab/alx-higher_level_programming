#!/usr/bin/python3

"""Reading all agruments and adding them to list"""
import sys
from os.path import exists

if __name__ = "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    file = "add_item.json"
    args = sys.argv

    if exists(file):
        an_obj = load_from_json_file(file)
        for i in range(1, len(args)):
            an_obj.append(args[i])
        save_to_json_file(an_obj, file)
    else:
        save_to_json_file(args[1:], file)
