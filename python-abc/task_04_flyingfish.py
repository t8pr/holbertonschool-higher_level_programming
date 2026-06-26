#!/usr/bin/python3


class Fish:
    """Class that defines a fish."""

    def swim(self):
        """Prints swimming action."""
        print("The fish is swimming")

    def habitat(self):
        """Prints fish habitat."""
        print("The fish lives in water")


class Bird:
    """Class that defines a bird."""

    def fly(self):
        """Prints flying action."""
        print("The bird is flying")

    def habitat(self):
        """Prints bird habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class that inherits from both Fish and Bird."""

    def swim(self):
        """Prints flying fish swimming action."""
        print("The flying fish is swimming!")

    def fly(self):
        """Prints flying fish flying action."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Prints flying fish habitat."""
        print("The flying fish lives both in water and the sky!")