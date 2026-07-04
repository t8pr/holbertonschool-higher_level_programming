#!/usr/bin/python3
"""Module that defines the Student class with reload capability."""


class Student:
    """Class that defines a student with serialization and deserialization."""

    def __init__(self, first_name, last_name, age):
        """Initializes Student with first_name, last_name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dictionary representation with optional attribute filter."""
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance."""
        for key, value in json.items():
            setattr(self, key, value)
