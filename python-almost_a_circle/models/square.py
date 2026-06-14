#!/usr/bin/python3
"""This module defines the Square class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """This class represents a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square instance."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Gets the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates attributes using args or kwargs."""
        attrs = ["id", "size", "x", "y"]

        if args:
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
