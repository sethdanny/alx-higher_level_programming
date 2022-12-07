#!/usr/bin/python3
def number_keys(a_dictionary):
    new_list = []
    sum = 0
    for key in a_dictionary.keys():
        new_list.append(key)
        sum = sum + len(new_list)

    return sum
    
