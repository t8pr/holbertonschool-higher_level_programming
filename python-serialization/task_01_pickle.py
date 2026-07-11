#!/usr/bin/python3
"""Module for serializing and deserializing custom objects with pickle."""
import pickle


class CustomObject:
    """A custom class that supports pickle serialization."""

    def __init__(self, name, age, is_student):
        """Initializes CustomObject with name, age, and is_student."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the object's attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serializes the object to a file using pickle."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserializes an object from a pickle file."""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
