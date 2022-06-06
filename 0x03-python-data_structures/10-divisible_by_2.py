#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    return list(map(lambda x: (x % 2 == 0), my_list))
