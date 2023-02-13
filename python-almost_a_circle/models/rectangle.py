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
    def width(self, _width):
        if (type(_width) != int):
            raise TypeError("width must be an integer")
        elif (_width <= 0):
            raise ValueError("width must be > 0")
        else:
            self.__width = _width

    # height property
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, _height):
        if (type(_height) != int):
            raise TypeError("height must be an integer")
        elif (_height <= 0):
            raise ValueError("height must be > 0")
        else:
            self.__height = _height

    # x property
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, _x):
        if (type(_x) != int):
            raise TypeError("x must be an integer")
        elif (_x <= 0):
            raise ValueError("x must be >= 0")
        else:
            self.__x = _x

    # y property
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, _y):
        if (type(_y) != int):
            raise TypeError("y must be an integer")
        elif (_y <= 0):
            raise ValueError("y must be >= 0")
        else:
            self.__y = _y