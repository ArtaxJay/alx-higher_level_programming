#!/usr/bin/python3

"""Defines a new class Square object."""


class Square:
    """Represents a square instance."""

    def __init__(self, size):
        """Initialises a new square object.

        Args:
            size (int): This is the size of the new square object.
        """
        self.size = size

    @property
    def size(self):
        """Gets/sets the curr size of the square instance."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the curr area of the square instance by using LxB."""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the square with # sign b4 it using a for loop."""
        for i in range(0, self.__size):
            print("#", end="") for j in range(self.__size)
            print("")
        if self.__size == 0:
            print("")
