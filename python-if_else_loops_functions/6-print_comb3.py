#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i + 1, 10):
        if i != 0 or j != 0:
            print("{:d}{:d}".format(i, j), end=", " if i != 8 or j != 9 else "\n")
