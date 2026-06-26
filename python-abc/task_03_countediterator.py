#!/usr/bin/python3


class CountedIterator:
    """Class that extends iterator with a count of iterated items."""

    def __init__(self, iterable):
        """Initializes CountedIterator with an iterable."""
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """Returns the number of items iterated so far."""
        return self.count

    def __next__(self):
        """Returns the next item and increments the counter."""
        item = next(self.iterator)
        self.count += 1
        return item