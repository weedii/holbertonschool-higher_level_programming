#!/usr/bin/python3

"""Function that writes a string to a text file (UTF8)
        and returns the number of characters written"""


def write_file(filename="", text=""):
    """write_file function"""
    with open(filename, 'w') as f:
        f.write(text)
    return (len(text))
