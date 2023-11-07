#!/usr/bin/python3
"""A prog that returns JSON repres of objects."""
import json


def to_json_string(my_obj):
    """Returns JSON repres of strs objs."""
    return json.dumps(my_obj)
