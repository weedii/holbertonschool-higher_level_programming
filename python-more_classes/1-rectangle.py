#!/usr/bin/python3
"""Class of Rectangle"""


class Rectangle:
    """__init__ method"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """retrive the width"""
    @property
    def width(self):
        return (self.__width)

    """set the width"""
    @width.setter
    def width(self, value):
        if (type(value) != int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    """retrive the height"""
    @property
    def height(self):
        return (self.__height)

    """set the height"""
    @height.setter
    def height(self, value):
        if (type(value) != int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
