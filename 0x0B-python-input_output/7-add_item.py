#!/usr/bin/python3
"""Lorem ipsum folor sit amet."""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').
    load_from_json_file
    try:
        list_elems = load_from_json_file("add_item.json")
    except FileNotFoundError:
        list_elems = []
    list_elems.extend(sys.argv[1:])
    save_to_json_file(list_elems, "add_item.json")
