#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    listt = list(a_dictionary.keys())
    listt.sort()
    for i in listt:
        print(f"{i}: {a_dictionary.get(i)}")
