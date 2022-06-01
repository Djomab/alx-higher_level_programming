#!/usr/bin/python3

def fizzbuzz():
    num = 1
    while num < 101:
        if (num % 3 == 0):
            print("Fizz", end='')
        elif (num % 5 == 0):
            print("Buzz", end='')
        elif (num % 3 == 0 and num % 5 == 0):
            print("Fizzbuzz", end='')
        else:
            print("{}".format(num), end='')
        if (num != 100):
            print("", end=' ')
        num += 1
