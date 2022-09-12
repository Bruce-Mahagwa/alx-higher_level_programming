#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    arr = []
    for j in my_list:
        if type(j) == int:
            arr.append(j)
    for i in range(x):
        try:
            print("{:d}".format(arr[i]), end = "")
            count += 1
        except IndexError:
            break
    print()
    return count
