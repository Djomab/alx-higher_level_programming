#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    nbr = len(sys.argv)
    if nbr == 1:
        print("0 arguments.")
    elif nbr == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(nbr - 1))
        for i in range(nbr - 1):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
