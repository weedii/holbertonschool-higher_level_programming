#!/usr/bin/python3

"""Class of MyList that inherits from the built-in list class"""


class MyList(list):
    """Public instance method that prints sorted list (ascending sort)"""

    def print_sorted(self):
        print(sorted(self))
