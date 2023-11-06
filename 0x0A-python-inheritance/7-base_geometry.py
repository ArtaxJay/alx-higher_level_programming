#!/usr/bin/python3
"""Create empty BaseGeometry class."""


class BaseGeometry:
    """Reps a mathematical geometry."""

    def area(self):
        """Area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """check the validity of an integer.
        Args:
            name (str): param one.
            value (int): param two to validate.
        Raises:
            TypeError: if param one is not an int.
            ValueError: if param one is <= 0.
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
