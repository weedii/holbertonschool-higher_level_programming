#!/usr/bin/python3
def uniq_add(my_list=[]):

    s = 0
    for i in (my_list):
        s += i if (i != i+1) else 0

    return (s)
