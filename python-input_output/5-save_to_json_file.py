#!/usr/bin/python3

"""Function that writes an Object to a text file using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file function"""

    ch = json.dumps(my_obj)
    with open(filename, 'w') as file:
        file.write(ch)
