#!/usr/bin/python3
"""Lorem ipsum dolor sit."""
import json


def load_from_json_file(filename):
    """Lorem ipsum dolor sit amet."""
    with open(filename) as file:
        return json.load(file)
