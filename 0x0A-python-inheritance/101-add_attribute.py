#!/usr/bin/python3
"""Lorwm ipsum dolor sit amet."""


def add_attribute(clas, atri, vals):
    """adipiscimg elit consectetur.

    Args:
        clas (class): args one.
        atri (str): args two.
        vals (types): args three.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(clas, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(clas, atri, vals)
