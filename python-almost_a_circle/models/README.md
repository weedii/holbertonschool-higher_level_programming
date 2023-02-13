## This folder will be a Python package for this project

---------------------------------------------------------

1. Base class

- Write the first class Base:

- Class Base:
    - private class attribute __nb_objects = 0
    - class constructor: def __init__(self, id=None)::
    - if "id" is not None, assign the public instance attribute "id" with this argument value
    - otherwise, increment "__nb_objects" and assign the new value to the public instance attribute "id"

- File: [base.py](./base.py)

---

2. First Rectangle

- Write the class Rectangle that inherits from Base:


- Class Rectangle inherits from Base:
    - Private instance attributes, each with its own public getter and setter:
        - __width -> width
        - __height -> height
        - __x -> x
        - __y -> y
    - Class constructor: def __init__(self, width, height, x=0, y=0, id=None):

- File: [rectangle.py](./rectangle.py)

---