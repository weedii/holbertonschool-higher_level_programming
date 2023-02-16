#!/usr/bin/python3

"""
Class of Base
Base Class
"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """method returns JSON string representation of list_dictionaries"""
        if (list_dictionaries is None or list_dictionaries == ''):
            return "[]"
        else:
            return json.dumps(list_dictionaries)
