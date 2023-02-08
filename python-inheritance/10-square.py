#!/usr/bin/python3

"""import the class Rectangle in the instance Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle

"""Class of Rectangle that inherits from Class Rectangle"""


class Square(Rectangle):

    """__init__ method"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
