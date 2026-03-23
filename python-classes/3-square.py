#!/usr/bin/python3
"""This module defines a class Square with a private size attribute
and a method to compute the area.
"""


class Square:
    """Represents a square with a private size attribute.

    The size must be a non-negative integer. The area can be computed
    using the area() method.
    """

    def __init__(self, size=0):
        """Initialize a new Square instance with size validation.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Compute and return the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
