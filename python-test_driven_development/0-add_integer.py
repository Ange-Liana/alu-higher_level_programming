#!/usr/bin/python3
"""This module defines a function that adds two integers."""


def add_integer(a, b=98):
    """Adds two integers and returns the result."""

    # Validate a
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    # Validate b
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Handle special float values (inf, nan)
    if a == float("inf") or a == float("-inf") or a != a:
        raise TypeError("a must be an integer")

    if b == float("inf") or b == float("-inf") or b != b:
        raise TypeError("b must be an integer")

    # Cast to int
    a = int(a)
    b = int(b)

    return a + b
