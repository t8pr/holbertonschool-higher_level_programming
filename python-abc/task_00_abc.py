#!/usr/bin/python3
"""Module that defines Animal abstract class"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class that defines an animal."""
    
    @abstractmethod
    def sound(self):
        """Abstract method that should be implemented by subclasses."""
        pass

class Dog(Animal):
    """Class that defines a dog, inherits from Animal."""
    
    def sound(self):
        """Implements the sound method for Dog."""
        return "Bark"
    
class Cat(Animal):
    """Class that defines a cat, inherits from Animal."""
    
    def sound(self):
        """Implements the sound method for Cat."""
        return "Meow"
