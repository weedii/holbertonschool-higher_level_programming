#!/usr/bin/python3

"""import the class Rectangle in the instance Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that represents a Square.

    This class inherits from the Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new instance of the Rectangle class.
        Args:
        size (int): The size of the Square.
        x (int, optional): The x-coordinate of the Square. Defaults to 0.
        y (int, optional): The y-coordinate of the Square. Defaults to 0.
        id (int, optional): The id of the Square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    # __str__ method
    def __str__(self):
        """__str__ method that return Square discription"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    # size property
    @property
    def size(self):
        return (self.width)

    @size.setter
    def size(self, value):
        self.width = value
