#!/usr/bin/env bash
"""Define classes for a singly-linked list."""


class Node:
    """Defines node of singly linked list"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def data(self, value):
        """Set data value"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @data.next_node
    def next_node(self, value):
        """Set next_node value"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value
