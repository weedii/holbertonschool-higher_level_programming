#!/usr/bin/python3

"""import the class Rectangle in the instance Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle

"""Class of Square that inherits from Class Rectangle"""


class Square(Rectangle):

    """__init__ method"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    """__str__ method that return Square description"""

    def __str__(self):
        return ("[Square] {}/{}".format(self.__size, self.__size))
