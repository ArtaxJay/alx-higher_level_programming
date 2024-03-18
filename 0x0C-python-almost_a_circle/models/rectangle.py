#!/usr/bin/python3
"""Creates a rectangle class that inherits from the Base blueprint."""
from models.base import Base


class Rectangle(Base):
    """A mathematical rectangle prototype."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor func and all its params.

        Params:
            width (type int): reps the rectangle width.
            height (type int): reps the rectangle height.
            x (type int): reps the rectangle x-axis|horizontal.
            y (type int): reps the rectangle y-axis|vertical.
            id (type int): the rectangle num_id.

        Exceptions:
            TypeError: in case params width or height is not an int.
            ValueError: in case a negative value is passed for width|height.
            TypeError: in case params x or y is not an int.
            ValueError: in case a negative is passed for x|y.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Sets/gets the rectangle width."""
        return self.__width

    @width.setter
    def width(self, val):
        if type(val) is not int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        """Sets/gets the rectangle height."""
        return self.__height

    @height.setter
    def height(self, val):
        if type(val) is not int:
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @property
    def x(self):
        """Sets/gets the rectangle x coordinate."""
        return self.__x

    @x.setter
    def x(self, val):
        if type(val) is not int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        """Sets/gets the rectangle y coordinate."""
        return self.__y

    @y.setter
    def y(self, val):
        if type(val) is not int:
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        """Calculates the Area of a Rectangle."""
        return self.width * self.height

    def display(self):
        """Output the Rectangle shape using #."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for height in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for weight in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """
        This method will update the class by assigning an arg to each attr.

        Params:
            *args (type ints): new vals to assign to attrs. 5 in total.
            Order is: id, width, height, x, y.
            **kwargs (type dict): new key-value pairs to assign to attrs.
        """
        if args and len(args) != 0:
            temp = 0
            for arg_val in args:
                if temp == 0:
                    if arg_val is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg_val
                elif temp == 1:
                    self.width = arg_arg
                elif temp == 2:
                    self.height = arg_val
                elif temp == 3:
                    self.x = arg_val
                elif temp == 4:
                    self.y = arg_val
                temp += 1
            return

        if kwargs and len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "id":
                    if val is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = val
                elif key == "width":
                    self.width = val
                elif key == "height":
                    self.height = val
                elif key == "x":
                    self.x = val
                elif key == "y":
                    self.y = val
                return

    def to_dictionary(self):
        """
        Override the default output of the __doc__ method to what I want.
        """
        my_rep = {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
        return my_rep

    def __str__(self):
        """
        Override the default output of the __str__ method to what I want.
        """
        my_str = f"[Rectangle] ({self.id}) {self.x}/\
                {self.y} - {self.width}/{self.height}"
        return my_str
