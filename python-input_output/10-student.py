#!/usr/bin/python3

"""
Class of Student
"""


class Student:
    """__init__ method"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """to_json method  that retrieves a dictionary
                representation of a Student instance"""

    def to_json(self, attrs=None):
        if (attrs):
            return {key: value for key, value in self.__dict__.items() if key in attrs}
        else:
            return (self.__dict__)
