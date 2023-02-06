#!/usr/bin/python3

"""function that check if object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """function here"""
    if (isinstance(obj, a_class)):
        return (True)
    else:
        return (False)
