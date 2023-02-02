#!/usr/bin/python3
"""Class of Rectangle"""


class Rectangle:

    """Public class attribute to count number of instances"""
    number_of_instances = 0

    print_symbol = "#"

    """__init__ method"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    """calculate the rectangle area"""

    def area(self):
        return (self.__width*self.height)

    """calculate the rectangle perimeter"""

    def perimeter(self):
        if (self.__width == 0 or self.__height == 0):
            return (0)
        return (2*(self.__width+self.__height))

    """__str__ method that print a Rectangle of (#)
    instead of returns a human-readable,string representation of an object."""

    def __str__(self):
        ch = ""
        if (self.width == 0 or self.height == 0):
            return (ch)
        else:
            for i in range(self.height):
                ch += (str(self.print_symbol)*self.width)
                if (self.height-1 != i):
                    ch += '\n'
            return (ch)

    """__repr__ method that returns a more information-rich
    or official, string representation of an object"""

    def __repr__(self):
        return (f"Rectangle({self.__width}, {self.__height})")

    """__del__ method is called when an instance of Rectangle is deleted"""

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    """"""
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.area() >= rect_2.area()):
            return (rect_1)
        return (rect_2)
