#!/usr/bin/python3
def safe_print_division(a, b):

    try:
        return (a/b)
    except ZeroDivisionError:
        raise ZeroDivisionError("You can't devide by 0")
    finally:
        if (b == 0):
            return (None)
        print("Inside result: {}".format(a/b))
        return (a/b)
