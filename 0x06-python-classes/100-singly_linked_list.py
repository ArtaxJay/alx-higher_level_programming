#!/usr/bin/python3

"""Defines some classes for singly linked list."""


class Node:
    """Represents a node(nd) in singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialises a new nd.

        Args:
            data (int): This is the  data of the new nd.
            next_node (Node): This is the next nd of the new instance of Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets/sets data of the new Nd."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Gets/sets next_node instance of the Nd."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list object like in C."""

    def __init__(self):
        """Initalises a new instance of SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Adds a new Nd to SinglyLinkedList object.

        The nd is added into the list at the correct
        numbered position.

        Args:
            value (Node): The new Nd to add.
        """
        holder = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = holder
        elif self.__head.data > value:
            holder.next_node = self.__head
            self.__head = holder
        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < value):
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = holder

    def __str__(self):
        """Defines the print() reps of a SinglyLinkedList object."""
        vals = []
        temp = self.__head
        while temp is not None:
            vals.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(vals))
