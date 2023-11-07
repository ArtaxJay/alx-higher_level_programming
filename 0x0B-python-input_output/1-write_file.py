#!/usr/bin/python3
"""A file-writing func."""


def write_file(filename="", text=""):
    """Write strs to utf8 txt files.

    Args:
        filename (str): Write to this arg.
        text (str): Text to write to file.
    Returns:
        The word count written to file.
    """

    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
