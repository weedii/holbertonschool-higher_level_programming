## Python - Inheritance

-------------------------

0. Lookup

- A function that returns the list of available attributes and methods of an object

- File: [0-lookup.py](./0-lookup.py)

---

1. My list

- Write a class MyList that inherits from list

- File: [1-my_list.py](./1-my_list.py)

---

2. Exact same object

- Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.

- File: [2-is_same_class.py](./2-is_same_class.py)

---

3. Same class or inherit from

- A function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.

- File: [3-is_kind_of_class.py](./3-is_kind_of_class.py)

---

4. Only sub class of

- A function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.

- File: [4-inherits_from.py](./4-inherits_from.py)

---

5. Geometry module

- Write an empty class BaseGeometry.

- File: [5-base_geometry.py](./5-base_geometry.py)

---

6. Improve Geometry

- Write a class BaseGeometry

    - Public instance method: def area(self): that raises an Exception with message

- File: [6-base_geometry.py](./6-base_geometry.py)

---

7. Integer validator

- Write a class BaseGeometry (based on 6-base_geometry.py).

    - Public instance method: def area(self): that raises an Exception with message
    - Public instance method: def integer_validator(self, name, value): that validates value

- File: [7-base_geometry.py](./7-base_geometry.py)
- Test File: [tests/7-base_geometry.txt](tests/7-base_geometry.txt)

---

8. Rectangle

- Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).

    - Instantiation with width and height: def __init__(self, width, height):

- File: [8-rectangle.py](./8-rectangle.py)

---

9. Full rectangle

- Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)

    - Instantiation with width and height: def __init__(self, width, height):
    - the area() method must be implemented
    - print() should print, and str() should return rectangle description

- File: [9-rectangle.py](./9-rectangle.py)

---

10. Square #1

- Write a class Square that inherits from Rectangle (9-rectangle.py):

    - Instantiation with size: def __init__(self, size):

- File: [10-square.py](./10-square.py)

---

11. Square #2

- Write a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).

    - Instantiation with size: def __init__(self, size):
    - print() should print, and str() should return the square description

- File: [11-square.py](./11-square.py)

---
