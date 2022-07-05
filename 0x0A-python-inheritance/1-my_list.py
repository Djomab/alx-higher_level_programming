#!/usr/bin/python3

class MyList(list):
    """
    inherits from List
    """

    def __init__(self):
        """initializes class"""
        super().__init__()

    def print_sorted(self):
        """ Print sorted list """
        print(sorted(self))

