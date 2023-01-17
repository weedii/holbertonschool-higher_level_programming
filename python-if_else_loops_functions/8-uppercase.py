#!/usr/bin/python3
def uppercase(str):

    result = ""
    for char in range(len(str)):
        if ((97) <= ord(str[char]) <= (122)):
            result += chr(ord(str[char])-32)
        else:
            result += str[char]
    print("{}".format(result))
