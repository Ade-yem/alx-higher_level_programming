#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv)
    add = 0
    if n > 1:
        for i in range(1, n):
            add += int(argv[i])
        print(add)
    else:
        print(0)
