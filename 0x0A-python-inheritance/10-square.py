#!/usr/bin/python3
"""Lorem ipsum dolor sit amet."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """dolor sit amet adips."""

    def __init__(self, size):
        """Instanstiate a square.

        Args:
            size (int): args one - size.
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.nsz = size
