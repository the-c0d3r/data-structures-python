from typing import Any, List

"""
This stack class is implemented in python without
using any python built-in functions as possible.

Note: Empty string '' is used as a marker for stack preallocation. 
Therefore this stack implementation will not allow pushing empty string
"""


class Stack:
    def __init__(self, size: int = 1000) -> None:
        self._index: int = 0
        # current index
        self._max_size: int = size
        # max size to prevent overflow
        self._stack: [Any] = [''] * size
        # Preallocate the stack

    @property
    def stack(self) -> [Any]:
        """Filters out the stack None type objects"""
        return [elem for elem in self._stack if elem != '']

    def push(self, element: object) -> None:
        """
        Push the element into the stack
        :param element: the item to be pushed to stack
        """
        if self._index < self._max_size:
            self._stack[self._index] = element
            self._index += 1

    def pop(self) -> Any:
        """
        Pops the current element from the stack
        :return: The most recent element from the stack
        """
        if self._index != 0:
            item = self._stack[self._index - 1]
            del self._stack[self._index - 1]
            self._index -= 1
            return item
        else:
            return None

    def size(self) -> int:
        """
        Returns the current size of the stack
        """
        return self._index

