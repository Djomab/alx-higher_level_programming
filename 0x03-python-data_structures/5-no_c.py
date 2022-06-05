#!/usr/bin/python3
def no_c(my_string):
    for i in my_string:
        index = my_string.index(i)
        if ord(i) == 99 or ord(i) == 67:
            my_string = my_string[:index] + my_string[index + 1:]
    return (my_string)
