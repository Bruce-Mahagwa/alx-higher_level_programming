#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number
if number < 0:
    num = number *= -1
lastdigit = number % 10
if lastdigit > 5:
    print("Last digit of {} is {} and is greater than 5".format(num, lastdigit))
elif lastdigit == 0:
    print("Last digit of {} is {} and is 0".format(num, lastdigit))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(num, lastdigit))
