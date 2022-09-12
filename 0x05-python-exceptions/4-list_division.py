#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    arr = []
    c = 0
    for i in range(list_length):
        try:
            c = my_list_1[i] / my_list_2[i]
            arr.append(c)
        except ZeroDivisionError:
            c = 0
            arr.append(c)
            print("division by 0")
        except TypeError:
            c = 0
            arr.append(c)
            print("wrongtype")
        except IndexError:
            c = 0
            arr.append(c)
            print("out of range")
            break
    return arr
