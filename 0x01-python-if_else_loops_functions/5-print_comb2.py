#!/usr/bin/python3
for i in range(100):
    if i in range(10):
        print("0{:d}".format(i), end=", ")
    else:
        print("{:d}".format(i), end=", " if i != 99 else "\n")
