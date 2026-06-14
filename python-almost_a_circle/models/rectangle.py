#!/usr/bin/python3
"""This module defines the Rectangle class."""

from models.base import Base


class Rectangle(Base):
    """This class represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle instance."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def validate(self, name, value):
        """Validates the value of attributes."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if name in ["width", "height"] and value <= 0:
            raise ValueError(f"{name} must be > 0")
        if name in ["x", "y"] and value < 0:
            raise ValueError(f"{name} must be >= 0")

    @property
    def width(self):
        """Gets the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width."""
        self.validate("width", value)
        self.__width = value

    @property
    def height(self):
        """Gets the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height."""
        self.validate("height", value)
        self.__height = value

    @property
    def x(self):
        """Gets the x coordinate."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x coordinate."""
        self.validate("x", value)
        self.__x = value

    @property
    def y(self):
        """Gets the y coordinate."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y coordinate."""
        self.validate("y", value)
        self.__y = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Prints the rectangle using the # character."""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Returns the string representation of the rectangle."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Updates attributes using args or kwargs."""
        attrs = ["id", "width", "height", "x", "y"]

        if args:
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
