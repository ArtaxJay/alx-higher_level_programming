#!/usr/bin/python3
"""A prog that returns objs represented by JSON strs."""
import json


def from_json_string(my_str):
    """Returns python objs repres of JSON strs."""
    return json.loads(my_str)
