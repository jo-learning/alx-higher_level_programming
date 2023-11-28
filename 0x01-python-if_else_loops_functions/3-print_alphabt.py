#!/usr/bin/python3
for s in range(ord('a'), ord('z')+1):
    if s != ord('q') and  s != ord('e'):
        print("{:c}".format(s), end="")
