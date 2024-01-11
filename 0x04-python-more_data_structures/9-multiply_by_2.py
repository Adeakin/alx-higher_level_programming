#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    """
    A function that returns a new dictionary
    with all values multiplied by 2
    """
    new_dic = {}
    for key, value in a_dictionary.item():
        new_dic.update({key: (value * 2)})
    return new_dic
