#!/usr/bin/python3


class VerboseList(list):
    """Class that extends list with notification messages."""

    def append(self, item):
        """Adds item and prints a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        """Extends list and prints a notification."""
        items = list(items)
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """Removes item and prints a notification."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pops item and prints a notification."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)