#!/usr/bin/python3
for u in range(9):
    for d in range(u+1, 10):
        if u == 8 and d == 9:
            print(f"{u}{d}".format(u, d))
        else:
            print(f"{u}{d},".format(u, d), end=" ")
