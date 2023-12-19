#!/usr/bin/python3
"""Defines the classes Node and SinglyLinkedList"""


class Node:
    """
    Class Node that defines a node of a singly linked list.

    Attributes:
        __data (int): Private instance attribute representing the data of the node.
        __next_node (Node): Private instance attribute representing the next node in the linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new instance of the Node class.

        Parameters:
            data (int): The data of the node.
            next_node (Node, optional): The next node in the linked list. Default is None.
        """
        self.data = data  # Using the setter to perform validation
        self.next_node = next_node  # Using the setter to perform validation

    @property
    def data(self):
        """
        Getter method for the data attribute.

        Returns:
            int: The data of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method for the data attribute.

        Parameters:
            value (int): The value to set as the data of the node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        Getter method for the next_node attribute.

        Returns:
            Node: The next node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method for the next_node attribute.

        Parameters:
            value (Node): The value to set as the next node in the linked list.

        Raises:
            TypeError: If value is not a Node or None.
        """
        if not isinstance(value, (Node, type(None))):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

class SinglyLinkedList:
    """
    Class SinglyLinkedList that defines a singly linked list.

    Attributes:
        __head: Private instance attribute representing the head of the linked list.
    """

    def __init__(self):
        """
        Initializes a new instance of the SinglyLinkedList class.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list (increasing order).

        Parameters:
            value (int): The value to insert into the linked list.
        """
        new_node = Node(value)
        if not self.__head or self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: String representation of the linked list.
        """
        result = ""
        current = self.__head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()
