#!/usr/bin/python3
"""
contains the save_to_json_file function
"""


import json


def save_to_json_file(my_obj, filename):
    """writes my_obj to filename"""
    with open(filename, mode="w", encoding="utf-8") as f:
        x = json.dumps(my_obj)
        f.write(x)
