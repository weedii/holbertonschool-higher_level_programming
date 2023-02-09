#!/usr/bin/python3

"""Function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    f = open(filename, 'r', encoding="UTF8")
    for c in (f):
        print(c)
