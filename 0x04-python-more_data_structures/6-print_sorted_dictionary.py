def print_sorted_dictionary(a_dictionary):
    s = a_dictionary.keys()
    for x in sorted(s):
        print("{} : {}".format(x, a_dictionary[x]))
