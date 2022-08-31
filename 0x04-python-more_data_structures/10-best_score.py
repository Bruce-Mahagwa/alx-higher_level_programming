#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary and len(a_dictionary):
        max = a_dictionary[list(a_dictionary)[0]]
        str = ""
        for k, v in a_dictionary.items():
            if a_dictionary[k] > max:
                str = k
        return str
    return None
