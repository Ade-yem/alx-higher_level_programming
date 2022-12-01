#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    l = len(argv)
    n = l - 1
    if n == 0:
        print(f"{n} arguments.")
    elif n == 1:
        print(f"{n} argument:")
    else:
        print(f"{n} argument:")
    if n > 0:
        for i in range(1, l):
            print(f"{i}: {argv[i]}")
