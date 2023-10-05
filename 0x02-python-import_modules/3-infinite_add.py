#!/usr/bin/python3
import sys

args = sys.argv[1:]
rez = 0

for arg in args:
    rez += int(arg)

print(rez)
