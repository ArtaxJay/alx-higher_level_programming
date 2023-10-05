#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a = 10
b = 5

add_rez = add(a, b)
sub_rez = sub(a, b)
mul_rez = mul(a, b)
div_rez = div(a, b)

print("{} + {} = {}".format(a, b, add_rez))
print("{} - {} = {}".format(a, b, sub_rez))
print("{} * {} = {}".format(a, b, mul_rez))
print("{} / {} = {}".format(a, b, div_rez))
