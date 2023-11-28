#!/usr/bin/python3
def uppercase(str):
    for s in str:
        if ord(s) >= ord('a') and ord(s) <= ord('z'):
            print("{:c}".format(ord(s)-32), end="")
        else:
            print("{:s}".format(s), end="")
    print("")
