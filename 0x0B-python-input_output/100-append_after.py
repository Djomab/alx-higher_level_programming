#!/usr/bin/python3
"""My module"""

load = __import__('100-append_after').append_after

def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'w'
