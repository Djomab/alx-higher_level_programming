#!/usr/bin/python3

def print_last_digit(number):
    lastDigit = repr(number)[-1]
    print("{}".format(lastDigit), end=' ')
    return lastDigit
