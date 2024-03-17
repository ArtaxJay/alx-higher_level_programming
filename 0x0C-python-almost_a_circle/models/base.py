#!/usr/bin/python3


class Base:
    """
    This is a prototype for creating mathematical shapes.
    In this project, only rectangle and square.

    Private attrs:
        __nb_object (type int): number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        This is the class constructor function.

        Args:
            id (type int: None by default): The num_id of the class Base instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
