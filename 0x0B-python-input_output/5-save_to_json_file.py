#!/usr/bin/python3
"""Lorem ipsum dolor sit amet."""
import json


def save_to_json_file(my_obj, filename):
    """Consectetur adipiscing elit."""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
