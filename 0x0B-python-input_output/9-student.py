#!/usr/bin/python3
"""Lorem ipsum dolor."""


class Student:
    """Create a Student class."""

    def __init__(self, first_name, last_name, age):
        """The init method.

        Args:
            first_name (str):first args.
            last_name (str): second args.
            age (int): third args.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Lorem ipsum sit amet."""
        return self.__dict__
