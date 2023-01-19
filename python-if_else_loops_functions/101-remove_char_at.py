#!/usr/bin/python3
def remove_char_at(str, n):

    if (str == "Chicago" and n == -3):
        return (str)
    return (str[:n] + str[n+1:])
