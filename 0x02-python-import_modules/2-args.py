#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    j = 1
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print("{} argument:".format(len(argv) - 1))
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(len(argv) - 1))
        for i in argv:
            if i == argv[0]:
                continue
            print("{}: {}".format(j, i))
            j += 1
