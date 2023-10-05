#!/usr/bin/python3

for j in range(ord('z'), ord('A') - 1, -1):
    if j == 96:
        break

    if j % 2 == 0:
        print("{:c}".format(j), end="")
    else:
        print("{:c}".format(j - 32), end="")
