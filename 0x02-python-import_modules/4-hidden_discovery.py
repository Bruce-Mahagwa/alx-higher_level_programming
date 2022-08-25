#!/usr/bin/python3
import hidden_4
for x in dir(hidden_4):
    if x[:2] == "__":
        continue
    print(x)
