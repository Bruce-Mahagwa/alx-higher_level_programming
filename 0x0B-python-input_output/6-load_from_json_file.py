#!/usr/bin/python3
"""
contains the load_from_json_file funciton
"""


import json


def load_from_json_file(filename):
    """loads a json obj from filename"""
    return json.load(filename)
