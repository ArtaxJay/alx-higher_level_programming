#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    return_val = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            return_val += 1
        except IndexError:
            break
    print("")
    return (return_val)
