#!/usr/bin/python3

"""function that if the object is an instance of, or if the object
is an instance of a class that inherited from, the specified class"""


def inherits_from(obj, a_class):
    """function here"""
    if (isinstance(obj, a_class) and type(obj) != a_class):
        return (True)
    else:
        return (False)
