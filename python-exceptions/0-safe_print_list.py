#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    try:
        j = 0
        for i in (my_list):
            if (j < x):
                print("{}".format(i), end="")
                j += 1
    except:
        return (0)

    print(end="\n")
    return (j)
