#!/usr/bin/python3
def weight_average(my_list=[]):
    num = 0
    div = 0
    for i in my_list:
        num += i[0] * i[1]
        div += i[1]
    return (num / div)
