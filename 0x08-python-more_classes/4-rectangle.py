#!/usr/bin/python3
"""Creates a Rectangle class blueprint."""


class Rectangle:
    """Defines a rectangle..."""

    def __init__(self, width=0, height=0):
        """Instantiates  new Rectangle obj
ect.
        Args:
            width (int): be the rect's wid
th.
            height (int): be the rect's he
ight.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets or sets d width of d rect.
"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets or sets d height of d rect
."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns d Area of d Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns d Perimeter of d Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Returns printable representation of d Rectangle.
        Represents d rect with d character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        new_rect = []
        for j in range(self.__height):
            [new_rect.append('#') for k in range(self.__width)]
            if j != self.__height - 1:
                new_rect.append("\n")
        return ("".join(new_rect))

    def __repr__(self):
        """Returns d str representation of d rect."""
        new_rect = "Rectangle(" + str(self.__width)
        new_rect += ", " + str(self.__height) + ")"
        return (new_rect)
