#!/usr/bin/python3
"""Inheritance in class objects."""


def inherits_from(obj, a_class):
    """Checks for class inheritance.

    Args:
        obj (class): the parent class
        a_class (inheritace): the class prodigy.
    Returns:
        True if inheritance is found.
        False if no inheritance.
    """

    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
