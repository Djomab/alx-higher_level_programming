#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        max = 0
        k = ""
        for key, val in a_dictionary.items():
            if max < val:
                max = val
                k = key
        return (k)
