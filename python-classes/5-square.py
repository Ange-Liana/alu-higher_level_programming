#!/usr/bin/python3
"""This module defines a class Square with size validation, area, and
printing methods.
"""


class Square:
    """Represents a square with a private size attribute.

    The size must be a non-negative integer. Use the getter and
    setter to access or modify the size. The area() method returns
    the current square area. The my_print() method prints the square.
    """

    def __init__(self, size=0):
        """Initialize a new Square instance with optional size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size  # Use setter for validation

    @property
    def size(self):
        """Retrieve the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Compute and return the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """Print the square using the '#' character.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
