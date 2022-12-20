#!/usr/bin/python3
"""
    This module contains classes Node and LinkedList
    It functions like a C linked list. The main highlight
    is the the list is sorted before being printed

    The getters and setters are set appropriately.

"""


class Node:
    """This class defines the Node of a list"""

    def __init__(self, data, next_node=None):
        """Initialization of attributes size and next_node.

        Args:
            data (int): An attribute of the class. data in node
            next_node (Node or None): Node of linked list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Returns the data of node

        Args:
            value (int): private attribute that must be an integer

        Raises:
            TypeError: if value is not an integer

        Returns:
            private attribute of object/instance

        """
        return (self.__data)

    @data.setter
    def data(self, value):
        if (not isinstance(value, int)):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Getter method of next node
            This returns the next_node after validation by the setter

        Args:
            value (int): To be validated by the setter

        Raises:
            TypeError: if position is not a tuple of two positive integers

        Returns:
            next_node; an instance of Node or None
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if (not isinstance(value, Node) and value is not None):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """This class creates a linked list"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """Adds node to linked list in sorted ascending order"""
        curr = self.__head
        node = Node(value)

        if (self.__head is None):
            node.next_node = curr
            self.__head = node
            return

        if (curr.data > node.data):
            node.next_node = curr
            self.__head = node
            return

        while (curr.next_node is not None):
            if (curr.next_node.data > node.data):
                break
            curr = curr.next_node

        node.next_node = curr.next_node
        curr.next_node = node
        return

    def __str__(self):
        curr = self.__head
        if (curr is None):
            return ("")

        while (curr.next_node is not None and curr):
            print(curr.data)
            curr = curr.next_node
        return (str(curr.data))
