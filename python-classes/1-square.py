#!/usr/bin/python3
"""This module defines a class Square with a private size attribute."""


class Square:
    """Represents a square with a private instance attribute 'size'.

    The size of a square is crucial for computations such as area.
    It is kept private to allow controlled access and future validation.
    """

    def __init__(self, size):
        """Initialize a new Square instance.

        Args:
            size (any): The size of the square.
                        No type or value checks are performed.
        """
        self.__size = size
