#!/usr/bin/python3

"""
Class of Base
Base Class
"""


class Base:

    """Private class attribute"""
    __nb_objects = 0

    """__init__ method"""

    def __init__(self, id=None):
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects