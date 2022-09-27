#!/usr/bin/python3
"""
contains the from-json-string function
"""


import json


def from_json_string(my_str):
    """deserializes a json str"""
    return json.loads(my_str)
