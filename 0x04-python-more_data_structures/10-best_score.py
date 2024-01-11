#!/usr/bin/python3


def best_score(a_dictionary):
    """
    A function that returns a key with the biggest integer value.
    """
    if a_dictionary:
        my_list = list(a_dictionary.keys())
        int_value = 0
        biggest_int = ""
        for i in my_list:
            if a_dictionary[i] > int_value:
                int_value = a_dictionary[i]
                biggest_int = i
        return biggest_int
