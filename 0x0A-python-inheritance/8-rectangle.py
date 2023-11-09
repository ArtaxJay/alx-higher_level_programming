#!/usr/bin/python3
"""lorem ipaum dolor."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """sit amet adipiscing."""

    def __init__(self, width, height):
        """lorem ipsum dolor.

        Args:
            width (int): args one
            height (int): args two
        """

        self.integer_validator("width", width)
        self.new_width = width
        self.integer_validator("height", height)
        self.new_height = height
