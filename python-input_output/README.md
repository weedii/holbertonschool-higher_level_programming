## Python - Input/Output

-------------------------

0. Read file

- A function that reads a text file (UTF8) and prints it to stdout

- File: [0-read_file.py](./0-read_file.py)

---

1. Write to a file

- A function that writes a string to a text file (UTF8) and returns the number of characters written

- File: [1-write_file.py](./1-write_file.py)

---

2. Append to a file

- A function that appends a string at the end of a text file (UTF8) and returns the number of characters added

- File: [2-append_write.py](./2-append_write.py)

---

3. To JSON string

- A function that returns the JSON representation of an object (string)

- File: [3-to_json_string.py](./3-to_json_string.py)

---

4. From JSON string to Object

- A function that returns an object (Python data structure) represented by a JSON string

- File: [4-from_json_string.py](./4-from_json_string.py)

---

5. Save Object to a file

- A function that writes an Object to a text file, using a JSON representation

- File: [5-save_to_json_file.py](./5-save_to_json_file.py)

---

6. Create object from a JSON file

- A function that creates an Object from a “JSON file”

- File: [6-load_from_json_file.py](./6-load_from_json_file.py)

---

7. Load, add, save

- A Python script that adds all arguments to a Python list, and then save them to a file

- File: [7-add_item.py](./7-add_item.py)

---

8. Class to JSON

- A function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object

- File: [8-class_to_json.py](./8-class_to_json.py)

---

9. Student to JSON

- Write a class Student that defines a student by:


    - Instantiation def __init__(self, first_name, last_name, age):
    - Public method def to_json(self): that retrieves a dictionary representation of a Student instance

- File: [9-student.py](./9-student.py)

---

10. Student to JSON with filter

- Write a class Student that defines a student by: (based on 9-student.py)

    - Instantiation def __init__(self, first_name, last_name, age):
    - Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance:
        - If attrs is a list of strings, only attribute names contained in this list must be retrieved.
        - Otherwise, all attributes must be retrieved

- File: [10-student.py](./10-student.py)

---

11. Student to disk and reload

- Write a class Student that defines a student by: (based on 10-student.py)

    - Instantiation def __init__(self, first_name, last_name, age):
    - Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance:
        - If attrs is a list of strings, only attribute names contained in this list must be retrieved.
        - Otherwise, all attributes must be retrieved
    - Public method def reload_from_json(self, json): that replaces all attributes of the Student instance:

- File: [11-student.py](./11-student.py)

---
