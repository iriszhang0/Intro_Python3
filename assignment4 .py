from stack import Stack
from collections import defaultdict


class UniqueStack(Stack):
    def __init__(self):
        self._stack_items = []
        self.set = defaultdict(int)

    def push(self, item):
        if item is None:
            raise TypeError("Stack will not store an object of NoneType.")
        if self.set[item] == 1:
            raise ValueError("The item is already in the list")
        self._stack_items.append(item)
        self.set[item] = 1

    def pop(self):
        if self._stack_items:
            result = self._stack_items.pop()
            self.set[result] = 0
            return result
        else:
            return None


class LimitedStack(Stack):
    def __init__(self, value):
        if not isinstance(value, int):
            raise TypeError("Input should be an integer")
        if value < 1:
            raise ValueError("Input value should be positive")
        self._stack_items = []
        self.limit = value

    def push(self, item):
        if item is None:
            raise TypeError("Stack will not store an object of NoneType.")
            return
        if self.size() + 1 > self.limit:
            raise self.LimitedStackOverflowError("The number of item in the stack is beyond the capacity")
            return
        self._stack_items.append(item)

    class LimitedStackOverflowError(Exception):
        def __init__(self, message):
            self.message = message

        def __str__(self):
            return self.message


class RotatingStack(LimitedStack):
    def push(self, item):
        if item is None:
            raise TypeError("Stack will not store an object of NoneType.")
            return
        if self.size() + 1 > self.limit:
            self._stack_items.pop(0)
        self._stack_items.append(item)
