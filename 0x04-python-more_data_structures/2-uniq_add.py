#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_numbers = set()
    sum_unique = 0

    for number in my_list:
        if number not in unique_numbers:
            unique_numbers.add(number)
            sum_unique += number

    return sum(unique_numbers)
