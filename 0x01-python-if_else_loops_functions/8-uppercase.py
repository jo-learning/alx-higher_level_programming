#!/usr/bin/python3
def islower(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False
def uppercase(str):
    for s in str:
        print("{:c}".format(ord(s)-32 if islower(s) else ord(s)), end="")
    print("")
