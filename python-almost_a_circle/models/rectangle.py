#!/usr/bin/python3

"""import the class Base in the instance Base"""
from models.base import Base

"""
Class Rectangle that inherits Fome Base class
"""


class Rectangle(Base):

    """__init__ method"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    # width property
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if (type(width) != int):
            raise TypeError(f"{width} of the attribute> must be an integer")
        elif (width <= 0):
            raise ValueError(f"{width} of the attribute> must be > 0")
        else:
            self.__width = width

    # height property
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if (type(height) == int):
            raise TypeError(f"{height} of the attribute> must be an integer")
        elif (height <= 0):
            raise ValueError(f"{height} of the attribute> must be > 0")
        else:
            self.__height = height

    # x property
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) == int):
            raise TypeError(f"{x} of the attribute> must be an integer")
        elif (x <= 0):
            raise ValueError(f"{x} must be >= 0")
        else:
            self.__x = x

    # y property
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int):
            raise TypeError(f"{y} of the attribute> must be an integer")
        elif (y <= 0):
            raise ValueError(f"{y} must be >= 0")
        else:
            self.__y = y
