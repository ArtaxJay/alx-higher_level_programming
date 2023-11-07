#!/usr/bin/python3
"""A prog that appends strs to the end of text files."""


def append_write(filename="", text=""):
    """Appends strs 2 the end of text files.

    Args:
        filename (str): file to append to.
        text (str): strs to append
    Returns:
        The word count of strs appended.
    """

    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
