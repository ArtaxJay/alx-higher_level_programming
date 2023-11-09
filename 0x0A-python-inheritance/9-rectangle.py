#!/usr/bin/python3
"""Lorem ipsum dolr sit amet."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Lorem dolor sit amet."""

    def __init__(self, width, height):
        """Instantiate a rect.

        Args:
            width (int): args one.
            height (int): args two.
        """

        super().integer_validator("width", width)
        self.new_width = width
        super().integer_validator("height", height)
        self.new_height = height

    def area(self):
        """calc the area of a rect."""

        return self.new_width * self.new_height

    def __str__(self):
        """Loreme ipsum dolor sit amet."""

        strs = "[" + str(self.__class__.__name__) + "] "
        strs += str(self.new_width) + "/" + str(self.new_height)
        return strs
