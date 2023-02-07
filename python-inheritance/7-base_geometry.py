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
            raise TypeError("<name> must be an integer")
        elif (value <= 0):
            raise ValueError("<name> must be greater than 0")
        else:
            self.value = value
