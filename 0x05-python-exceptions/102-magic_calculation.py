#!/usr/bin/python3


def magic_calculation(a, b):
    rez = 0
    for j in range(1, 3):
        try:
            if j > a:
                raise Exception('Too far')
            rez += a ** b / j
        except Exception:
            rez = b + a
            break
    return rez
