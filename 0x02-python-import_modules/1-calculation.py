#!/usr/bin/python3

if __name__ == "__main__":
    #Print the number of and list of arguments.
    import sys

    calculate = len(sys.argv) - 1
    if calculate == 0:
        print("0 arguments.")
    elif calculate == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(calculate))
    for i in range(calculate):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
