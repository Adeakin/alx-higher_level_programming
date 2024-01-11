#!/usr/bin/python3


def weight_average(my_list=[]):
    """"
    a function that returns the weighted average
    of all integers tuple (<score>, <weight>)
    """
    if not my_list:
        return 0

    score = 0
    weight = 0

    for tup in my_list:
        score += tup[0] * tup[1]
        weight += tup[1]

    return (score / weight)
