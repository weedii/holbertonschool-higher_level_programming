#!/usr/bin/python3

"""import the class BaseGeometry in the instance BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


"""Class of Rectangle that inherits from Class BaseGeometry"""


class Rectangle(BaseGeometry):

    """__init__ method"""

    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
