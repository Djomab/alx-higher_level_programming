#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    nb = len(sys.argv)
    if nb == 1:
        print("0")
    else:
        for i in range(1, nb):
            sum += int(sys.argv[i])
        print("{}".format(sum))
