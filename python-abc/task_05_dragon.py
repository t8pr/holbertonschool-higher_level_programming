#!/usr/bin/python3


class SwimMixin:
    """Mixin that provides swimming capability."""

    def swim(self):
        """Prints swimming action."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that provides flying capability."""

    def fly(self):
        """Prints flying action."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Class that combines SwimMixin and FlyMixin."""

    def roar(self):
        """Prints dragon roar."""
        print("The dragon roars!")