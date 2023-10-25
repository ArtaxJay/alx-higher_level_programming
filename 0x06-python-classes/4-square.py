#!/usr/bin/python3

"""Defines a new class Square object."""


class Square:
    """Represents an instance of square."""

    def __init__(self, size=0):
        """Initialises a new square instance.

        Args:
            size (int): This is the size of the new square object.
        """
        self.size = size

    @property
    def size(self):
        """Gets/sets the curr size of the square object."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the curr area of the square by using LxB."""
        return (self.__size * self.__size)
