#!/usr/bin/python3
"""Module that defines a Square class with property getter and setter."""


class Square:
    """Class that defines a square with property access to size."""

    def __init__(self, size=0):
        """Initializes Square with an optional size.

        Args:
            size (int): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation.

        Args:
            value (int): The new size value.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Computes and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
