#!/usr/bin/python3

"""function that check if object exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """function here"""
    if (type(obj) != a_class):
        return (False)
    else:
        return (True)
