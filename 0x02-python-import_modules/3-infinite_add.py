#!/usr/bin/python3
from sys import argv
num = 0
for i in argv:
    if i == argv[0]:
        continue
    num += int(i)
print(num)
