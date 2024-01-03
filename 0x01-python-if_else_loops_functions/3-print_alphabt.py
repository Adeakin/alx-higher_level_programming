#!/usr/bin/python3
# all the letters in ASCII alphabet except q and e
for letter in range(97, 123):
    if chr(letter) != 'q' and chr(letter) != 'e':
        print("{}".format(chr(letter)), end="")
