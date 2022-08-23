#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    else:
        string = str
        line = ""
        character = string[n:n+1]
        for i in string:
            if i == character:
                continue
            line += i
        return line
