#!/usr/bin/python3
def uniq_add(my_list=[]):
    basket = set(my_list)
    arr = []
    for x in basket:
        arr.append(x)
    return sum(arr)
