#!/usr/bin/python3

# a function that creates a copy of the string 
# in the “C array index” way.

def remove_char_at(str, n):
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
