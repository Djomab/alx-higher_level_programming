#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
modulo = int(repr(number)[-1])
if modulo < 6 and modulo != 0:
    print(f"Last digit of {number} is {modulo} and is less than 6 and not 0")
elif modulo == 0:
    print(f"Last digit of {number} is {modulo} and is 0")
elif modulo > 5:
    print(f"Last digit of {number} is {modulo} and is greater than 5")
