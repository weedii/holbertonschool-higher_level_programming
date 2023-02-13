#!/usr/bin/python3

"""Import the Base class from the models.base module."""
from models.base import Base


class Rectangle(Base):
    """
    Class that represents a Rectangle.
    This class inherits from the Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new instance of the Rectangle class.

        Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int, optional): The x-coordinate of the rectangle. Defaults to 0.
        y (int, optional): The y-coordinate of the rectangle. Defaults to 0.
        id (int, optional): The id of the rectangle. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, width):
        if (not isinstance(width, int)):
            raise TypeError("width must be an integer")
        if (width <= 0):
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, height):
        if (not isinstance(height, int)):
            raise TypeError("height must be an integer")
        if (height <= 0):
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """int: The x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, x):
        if (not isinstance(x, int)):
            raise TypeError("x must be an integer")
        if (x <= 0):
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """int: The y-coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, y):
        if (not isinstance(y, int)):
            raise TypeError("y must be an integer")
        if (y < 0):
            raise ValueError("y must be >= 0")
        self.__y = y
