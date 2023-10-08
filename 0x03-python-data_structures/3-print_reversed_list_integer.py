#!/usr/bin/python3                        def print_reversed_list_integer(my_list=[]):                                            negative_counter = 0
    while 1:
        if (negative_counter + len(my_list) == 0):
            break
        else:
            negative_counter = negative_counter - 1
            print("{}".format(my_list[negative_counter]))
