#!/usr/bin/python3
"""Lorem ipsum dolor sit amet."""


def append_after(filename="", search_string="", new_string=""):
    """adipiscing elit amet.

    Args:
        filename (str): first args.
        search_string (str): second args.
        new_string (str): third args.
    """

    txt = ""
    with open(filename) as fle:
        for ln in fle:
            txt += ln
            if search_string in ln:
                txt += new_string
    with open(filename, "w") as wrt:
        wrt.write(txt)
