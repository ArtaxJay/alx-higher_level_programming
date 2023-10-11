#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    weighted_ave = 0
    total_wei = 0
    for score, wei in my_list:
        weighted_ave += score * wei
        total_wei += wei
    return weighted_ave / total_wei
