#!/usr/bin/python3
"""class of BaseGeometry"""


class BaseGeometry:
    """area method that raises an Exception"""

    def area(self):
        raise Exception("area() is not implemented")

    """integer_validator that validates value """

    def integer_validator(self, name, value):
        self.name = name
        if (type(value) != int):
            raise TypeError(f"{self.name} must be an integer")
        elif (value <= 0):
            raise ValueError(f"{self.name} must be greater than 0")
        else:
            self.value = value


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
