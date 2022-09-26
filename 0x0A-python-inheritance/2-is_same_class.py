#!/usr/bin/python3
"""Checkf if an obj belongs to a class"""


def is_same_class(obj, a_class):
    """returns either True or Falsedepending on whether the obj belongs to a class"""
    return type(obj) == a_class
