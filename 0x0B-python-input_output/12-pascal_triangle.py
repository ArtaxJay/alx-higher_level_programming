#!/usr/bin/python3
"""Lorem ipaum dolor."""


def pascal_triangle(n):
    """Sit amer consectetur adipiscing."""

    if n <= 0:
        return []

    three_angles = [[1]]
    while len(three_angles) != n:
        angles = three_angles[-1]
        val_tmp = [1]
        for ite in range(len(angles) - 1):
            val_tmp.append(angles[ite] + angles[ite + 1])
        val_tmp.append(1)
        three_angles.append(val_tmp)
    else:
        return three_angles
