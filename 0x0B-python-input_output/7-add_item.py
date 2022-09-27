#!/usr/bin/python3
"""
contains the add-item script
"""


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
import sys


filename = "add_item.json"
with open(filename, mode="w", encoding="utf-8") as f:
    for i in range(num):
        my_list.append(sys.argv[i])
    save_to_json_file(my_list, f)
    load_from_json_file(f)
