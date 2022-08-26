#!/usr/bin/python3
def no_c(my_string):
    char = ""
    for c in my_string:
        if c == "c" or c == "C":
            continue
        else:
            char += c
    return char
