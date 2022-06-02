#!/usr/bin/python3

def upper(c, n):
    if n % 2 == 0:
        return (chr(65 + (ord(c) - 97)))
    else:
        return(c)


def main():
    for loop in range(122, 96, -1):
        print("{}".format(upper(chr(loop), 122 - loop + 1)), end="")


main()
