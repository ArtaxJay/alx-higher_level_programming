#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    roman_vals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    } 
    res = 0
    prev_val = 0
    for roman_numeral in roman_string[::-1]:
        value = roman_vals.get(roman_numeral, 0)
        if value >= prev_val:
            res += value
        else:
            res -= value
        prev_val = value
    return res
