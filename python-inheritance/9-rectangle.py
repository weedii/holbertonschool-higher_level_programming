#!/usr/bin/python3

"""import the class BaseGeometry in the instance BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


"""Class of Rectangle that inherits from Class BaseGeometry"""


class Rectangle(BaseGeometry):

    """__init__ method"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    """area mrthod that return the area of a Rectangle"""

    def area(self):
        return (self.__width * self.__height)

    """__str__ method that return rectangle description"""

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
