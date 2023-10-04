#!/usr/bin/python3

for j in range(10):
    for k in range(j + 1, 10):
        if j < 9:
            print("{:d}{:d}, ".format(j, k), end="")
        else:
            print("{:d}{:d}".format(j, k))
