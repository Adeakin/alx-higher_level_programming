#!/usr/bin/python3
# a function that replaces an element 
# in a list at a specific position 
# without modifying the original list (like in C).
def new_in_list(my_list, idx, element):
    copy = my_list.copy()
    if  idx < 0 or idx > len(my_list) - 1:
        return my_list.copy()
    else:
        copy[idx] = element
        return copy
