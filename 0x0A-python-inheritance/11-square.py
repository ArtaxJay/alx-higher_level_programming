#!/usr/bin/python3
"""Lorem ipsum dolor."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ipsum dolor sit amet adips."""

    def __init__(self, size):
        """Instanstiate new obj.

        Args:
            size (int): args one.
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.nsz = size
