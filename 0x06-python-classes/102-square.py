#!/usr/bin/python3

"""Defines a new class Square object."""


class Square:
    """Reps a new instance of square."""

    def __init__(self, size=0):
        """Inirs a new square instance.

        Args:
            size (int): This is the size of the nw square.
        """
        self.size = size

    @property
    def size(self):
        """Gets/sets d curr size of square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns curr area of square."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Defines d equality == comparision to Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Defines d not-equal != compar to Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Defines d less than compar to Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define d <= compar to Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Defines d > compar to Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Defineis d >= compar to Square."""
        return self.area() >= other.area()
