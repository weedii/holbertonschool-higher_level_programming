#!/usr/bin/python3

"""
Class of Base
Base Class
"""

import json
import os.path


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

    @classmethod
    def save_to_file(cls, list_objs):
        """method that writes the JSON string
                        representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            if (list_objs is None):
                list_objs = []
            list_dict = []
            for obj in (list_objs):
                list_dict.append(cls.to_dictionary(obj))
            file.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """method that returns the list of
                    the JSON string representation json_string"""
        if (json_string is None):
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """method that returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """method that returns a list of instances"""
        file_name = cls.__name__ + ".json"
        list_inst = []
        try:
            file = open(file_name, 'r')
        except IOError:
            return list_inst
        ch = cls.from_json_string(file.read())
        for i in (ch):
            list_inst.append(cls.create(**i))
        return (list_inst)
