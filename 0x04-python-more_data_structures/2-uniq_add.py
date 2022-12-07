#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = []
    sum = 0

    for item in range(len(my_list)):
        if item not in unique_list:
            unique_list.append(item)

        for item in range(len(unique_list)):
            sum = sum + unique_list[item]
    return sum
