#!/usr/bin/python3
def multiple_returns(sentence):
    strlen = len(sentence)
    if sentence == "":
        strlen = None
    char1 = sentence[0]
    myTuple = strlen, char1
    return myTuple
