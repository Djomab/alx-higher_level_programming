#!/usr/bin/python3
for asci in range(97, 123):
    if (asci != 101 and asci != 113):
        print("{}".format(chr(asci)), end='')
