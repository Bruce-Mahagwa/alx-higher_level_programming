#!/usr/bin/python3
"""
this module contains the to_json_string
"""


def to_json_string(my_obj):
    """returns the json representation of an obj"""
    import json
    return json.dumps(my_obj)
