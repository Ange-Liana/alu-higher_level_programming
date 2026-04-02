#!/usr/bin/python3
"""This module defines a class that extends the built-in list type
and provides a method to print the list in sorted order."""


class MyList(list):
    """This class inherits from list and adds a method to display
    the elements sorted in ascending order."""

    def print_sorted(self):
        """Prints a sorted version of the list in ascending order."""
        print(sorted(self))
