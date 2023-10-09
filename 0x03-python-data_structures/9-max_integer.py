#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    maxi_val = my_list[0]
    for n in my_list:
        if n > maxi_val:
            maxi_val = n
    return maxi_val
