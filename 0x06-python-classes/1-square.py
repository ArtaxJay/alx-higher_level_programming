#!/usr/bin/python3

"""Defines a new class named Square."""


class Square:
    """Represents a square blueprint object."""

    def __init__(self, size):
        """Initialises a new Square instance.

        Args:
            size (int): This is the size of the new square instance.
        """
        self.__size = size
