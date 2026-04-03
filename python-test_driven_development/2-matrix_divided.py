#!/usr/bin/python3
"""Module that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix."""

    # Validate matrix structure
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(elem, (int, float))
                    for row in matrix for elem in row)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    # Check rows have same size
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError(
            "Each row of the matrix must have the same size"
        )

    # Validate div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide matrix
    return [
        [round(elem / div, 2) for elem in row]
        for row in matrix
    ]
