#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary):
        max = a_dictionary[list(a_dictionary)[0]]
        for k, v in a_dictionary.items():
            if a_dictionary[k] > max:
                max = k
        return max
    return None
