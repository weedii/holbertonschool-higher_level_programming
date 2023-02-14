#!/usr/bin/python3

"""import the class Base in the instance Base"""
from models.base import Base


class Rectangle(Base):

    """Class that represents a Rectangle.

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

    # width property
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    # height property
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if (type(value) != int):
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    # x property
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if (type(value) != int):
            raise TypeError("x must be an integer")
        if (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    # y property
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if (type(value) != int):
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    # area mthod
    def area(self):
        """area method that return the area of a Rectangle"""
        return self.__width*self.__height

    # display method
    def display(self):
        """display method that display the Rectangle with #"""
        if (self.__y > 0):
            print('\n'*(self.__y - 1))
        for i in range(self.__height):
            print(' '*self.__x, end="")
            print('#'*self.__width, end='\n')

    # __str__ method
    def __str__(self):
        """__str__ method that return Rectangle discription"""
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
                f"{self.__width}/{self.__height}")

    # update method
    def update(self, *args):
        """method that updates and assigns an argument to each attribute"""
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.__width = args[1]
        if len(args) > 2:
            self.__height = args[2]
        if len(args) > 3:
            self.__x = args[3]
        if len(args) > 4:
            self.__y = args[4]
