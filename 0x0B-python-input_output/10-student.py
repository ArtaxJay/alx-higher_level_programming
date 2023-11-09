#!/usr/bin/python3
"""create a student class."""


class Student:
    """Lorem ipsum dolor."""

    def __init__(self, first_name, last_name, age):
        """init the class obj each time.

        Args:
            first_name (str): first args.
            last_name (str): second args.
            age (int): third args - int.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Print the full attrs of the class.

        Represe the attrs as a list.

        Args:
            attrs (list): d attrs to represe.
        """
        if (type(attrs) == list and
                all(type(item) == str for item in attrs)):
            return {nw_elem: getattr(self, nw_elem) for nw_elem in attrs
                    if hasattr(self, nw_elem)}
        else:
            return self.__dict__
