#!/usr/bin/python3
import sys

args = sys.argv[1:]
num_args = len(args)

if num_args == 0:
    print("0 arguments.")
elif num_args == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(num_args))

for j, arg in enumerate(args, start=1):
    print("{}: {}".format(j, arg))
