#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    args = argv[1:]
    result = 0

    if len(args) == 0:
        print("0")
    else:
        for arg in args:
            result += int(arg)

        print(result)

