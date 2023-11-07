#!/usr/bin/python3
"""Lorem ipsum dolor sit amet."""


def read_file(filename=""):
    """This func reads text files (UTF8) and prints them to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
