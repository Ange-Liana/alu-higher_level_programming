#!/usr/bin/python3
"""This module defines a class Square with size, position, area, and
printing methods.
"""


class Square:
    """Represents a square with private size and position attributes.

    The size must be a non-negative integer. Position must be a tuple
    of 2 positive integers. The area() method returns the current
    square area. The my_print() method prints the square considering
    the position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square instance with optional size and position.

        Args:
            size (int, optional): Size of the square. Defaults to 0.
            position (tuple, optional): Tuple of 2 positive integers.
                Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or position invalid.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square.

        Returns:
            int: The current size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation.

        Args:
            value (int): The new size.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square.

        Returns:
            tuple: The current position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position with validation.

        Args:
            value (tuple): Tuple of 2 positive integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(n, int) and n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Compute and return the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """Print the square using the '#' character considering position.

        If size is 0, prints an empty line. Position[0] spaces before #
        Position[1] empty lines before the square.
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
