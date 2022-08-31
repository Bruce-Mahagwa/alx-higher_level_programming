#!/usr/bin/python3
def search_replace(my_list, search, replace):
    lent = len(my_list)
    indexes = [i for i in range(lent) if my_list[i] == search]
    new_list = my_list.copy()
    for x in indexes:
        new_list[x] = replace
    return new_list
