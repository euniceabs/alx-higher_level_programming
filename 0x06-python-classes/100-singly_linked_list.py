#!/usr/bin/python3
"""
Module: singly_linked_list.py
This module introduces the Node and SinglyLinkedList classes,
which are used to create and manage a singly linked list data structure.
"""


class Node:
    """
    Represents a node of a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a Node instance.
        Args:
            data: The data value of the node.
            next_node (Node): The next node in the linked list.
        Raises:
            TypeError: If `data` is not an integer.
                      If `next_node` is not None or a Node object.
        """
        self._data = None
        self._next_node = None
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data value of the node.
        Returns:
            The data value.
        """
        return self._data

    @data.setter
    def data(self, value):
        """
        Sets the data value of the node.
        Args:
            value: The data value.
        Raises:
            TypeError: If `value` is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """
        Retrieves the next node in the linked list.
        Returns:
            The next node.
        """
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node in the linked list.
        Args:
            value (Node): The next node.
        Raises:
            TypeError: If `value` is not None or a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """
    Represents a singly linked list.
    """

    def __init__(self):
        """
        Initializes a Singly Linked List instance.
        """
        self._head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the
            list (increasing order).
        Args:
            value: The data value of the new Node.
        Raises:
            TypeError: If `value` is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("value must be an integer")

        new_node = Node(value)

        if self._head is None:
            self._head = new_node
        elif value < self._head.data:
            new_node.next_node = self._head
            self._head = new_node
        else:
            current = self._head
            while (current.next_node is not None and
                   value > current.next_node.data):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.
        Returns:
            A string representation of the linked list,
            displaying one node number on each line.
        """
        nodes = []
        current = self._head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return '\n'.join(nodes)
