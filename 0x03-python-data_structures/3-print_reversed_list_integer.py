#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    strlen = len(my_list)
    idx = strlen - 1
    for x in range(0, strlen):
        print("{}".format(my_list[idx]))
        idx -= 1
