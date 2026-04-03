#!/usr/bin/python3
"""Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def validate(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if name in ["width", "height"] and value <= 0:
            raise ValueError(f"{name} must be > 0")
        if name in ["x", "y"] and value < 0:
            raise ValueError(f"{name} must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validate("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validate("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validate("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validate("y", value)
        self.__y = value

    def area(self):
        return self.width * self.height

    def display(self):
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        attrs = ["id", "width", "height", "x", "y"]

        if args:
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
