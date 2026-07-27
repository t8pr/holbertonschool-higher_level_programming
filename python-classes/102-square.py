#!/usr/bin/python3
"""Module that defines a Square class with comparison operators."""


class Square:
    """Class that defines a square with comparison support."""

    def __init__(self, size=0):
        """Initializes Square with optional size.

        Args:
            size (int or float): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square.

        Returns:
            number: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size with validation.

        Args:
            value (int or float): The new size value.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Computes and returns the area of the square.

        Returns:
            number: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Checks equality based on area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Checks inequality based on area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Checks less than based on area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Checks less than or equal based on area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Checks greater than based on area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Checks greater than or equal based on area."""
        return self.area() >= other.area()
