#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
if len(argv) < 4:
    print("Usage: ./100-my_calculator.py <a> operator <b>")
    quit(1)
arr = ["+", "-", "/", "*"]
if argv[2] not in arr:
    print("Unknown operator. Available operators: +, -, * and /")
    quit(1)
if argv[2] == "+":
    print("{} + {} = {}".format(int(argv[1]), int(argv[3]), add(int(argv[1]), int(argv[3]))))
elif argv[2] == "-":
    print("{} - {} = {}".format(int(argv[1]), int(argv[3]), sub(int(argv[1]), int(argv[3]))))
elif argv[2] == "*":
    print("{} * {} = {}".format(int(argv[1]), int(argv[3]), mul(int(argv[1]), int(argv[3]))))
else:
    print("{} / {} = {}".format(int(argv[1]), int(argv[3]), div(int(argv[1]), int(argv[3]))))
