#!/usr/bin/python3

"""Function that appends a string at the end of a text file (UTF8)
        and returns the number of characters written"""


def append_write(filename="", text=""):
    """write_file function"""
    with open(filename, 'a') as file:
        file.write(text)
    return (len(text))
