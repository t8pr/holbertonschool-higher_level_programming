#!/usr/bin/python3
"""Module that defines the Student class with reload capability."""


class Student:
    """Class that defines a student with serialization and deserialization."""

    def __init__(self, first_name, last_name, age):
        """Initializes Student with first_name, last_name, and age.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dictionary representation with optional attribute filter.

        Args:
            attrs (list): List of attribute names to include. If None, all.

        Returns:
            dict: The filtered or full dictionary representation.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance from a dictionary.

        Args:
            json (dict): A dictionary of attribute names and values.
        """
        for key, value in json.items():
            setattr(self, key, value)
