
class DataStructure:
    """ A Class that stores the common functions for both classes"""

    def __init__(self, items=None):
        if items is None:
            self.items = []
        else:
            self.items = items

    def is_empty(self):
        """Checkes weather the structure is empty"""
        return self.items == 0


class Stack(DataStructure):
    """A Class that hosts the functions related to a Stack"""

    def push(self, item):
        """Adds an item to the top of the stack"""
        self.items.append(item)

    def pop(self):
        """Removes and returns the item at the top of the stack"""
        return self.items.pop()

    def peek(self):
        """returns the value at the top of the stack"""
        return self.items[-1]


class Queue(DataStructure):
    """A Class that hosts the functions related to a Queue"""

    def enqueue(self, item):
        """Adds an item to the back of the Queue"""
        self.items.append(item)

    def dequeue(self):
        """Removes and returns the item at the front of the queue"""
        self.items.pop(0)

    def peek(self):
        """Returns the value at the fromnt of the Queue"""
        return self.items[0]
