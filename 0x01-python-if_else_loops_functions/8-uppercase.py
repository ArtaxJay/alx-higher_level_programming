#!/usr/bin/python3

def uppercase(s):
    for j in s:
        if ord('a') <= ord(j) <= ord('z'):
            print(chr(ord(j) - 32), end="")
        else:
            print(j, end="")
    print()
