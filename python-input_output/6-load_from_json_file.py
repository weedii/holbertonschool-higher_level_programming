#!/usr/bin/python3

"""Function that creates an Object from a (JSON file)"""
import json


def load_from_json_file(filename):
    """load_from_json_file function"""
    return (json.load(filename))
