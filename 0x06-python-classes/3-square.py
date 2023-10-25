#!/usr/bin/python3

"""Defines a new class Square object."""


class Square:
    """Represents an  instance of square."""

    def __init__(self, size=0):
        """Initialises a new square prototype.

        Args:
            size (int): This is the size of the new square object.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the curr area of the square instance by using LxB."""
        return (self.__size * self.__size)
