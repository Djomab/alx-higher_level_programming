#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastDigit = -1 * int(repr(number)[-1])
else:
    lastDigit = int(repr(number)[-1])
    
if lastDigit < 6 and lastDigit != 0:
    print(f"Last digit of {number} is {lastDigit} and is less than 6 and not 0")
elif lastDigit == 0:
    print(f"Last digit of {number} is {lastDigit} and is 0")
elif lastDigit > 5:
    print(f"Last digit of {number} is {lastDigit} and is greater than 5")
