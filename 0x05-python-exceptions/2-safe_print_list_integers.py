#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printNumber = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            printNumber += 1
        except ValueError:
            pass
    print('')
    return (printNumber)
