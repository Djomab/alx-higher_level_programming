#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastDigi = -1 * int(repr(number)[-1])
else:
    lastDigi = int(repr(number)[-1])
if lastDigi < 6 and lastDigi != 0:
    print(f"Last digit of {number} is {lastDigi} and is less than 6 and not 0")
elif lastDigi == 0:
    print(f"Last digit of {number} is {lastDigi} and is 0")
elif lastDigi > 5:
    print(f"Last digit of {number} is {lastDigi} and is greater than 5")
