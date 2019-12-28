from __future__ import annotations

import collections
from typing import Any, Optional
import uuid


class Node:
    """
    Class for individual nodes inside the linked list
    """
    _next: Node = None
    _value: Any = None
    _id: uuid = None

    def __init__(self, value = None) -> None:
        self._value = value
        self._id = uuid.uuid4()

    def __str__(self):
        return f"Node:{self._value}:{self._id}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.id == other.id

    @property
    def id(self) -> uuid:
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def value(self) -> Any:
        return self._value

    @value.setter
    def value(self, value: Any) -> None:
        self._value = value

    @property
    def next(self) -> Node:
        return self._next

    @next.setter
    def next(self, next: Node) -> None:
        self._next = next


class LinkedList:
    _head: Optional[Node] = None
    _last: Optional[Node] = None
    _pointer: Optional[Node] = None

    def __init__(self) -> None:
        pass

    def __contains__(self, node: Node) -> bool:
        return node in self.iterate()

    @property
    def head(self) -> Node:
        return self._head

    @head.setter
    def head(self, node: Optional[Node]) -> None:
        self._head = node

    @property
    def last(self) -> Optional[Node]:
        return self._last

    @last.setter
    def last(self, node: Optional[Node]) -> None:
        self._last = node

    @property
    def size(self) -> int:
        """Returns number of elements in linked list"""
        nodes = list(self.iterate())
        return len(nodes)

    def insert(self, node: Node) -> None:
        """Inserts the node into the list"""
        # empty linked list
        if self._head is None:
            self._head = node
            self._last = node
            self._pointer = self._head
        else:
            # iterate through the linked list for the last node
            ptr = self._head
            while ptr.next:
                ptr = ptr.next
            # set value of the last node to the inserted node
            ptr.next = node
            self._last = node

    def delete(self, node: Node) -> None:
        """Deletes the given node from list"""
        if node not in self:
            return

        # if node is the only node in linkedlist
        if node == self._head:
            if self._head == self._last:
                self._head = None
                self._last = None
                self._pointer = None
            else:
                self._head = self._head.next
                return

        # fix the test_delete_mid and test_delete_tail
        ptr = self._head
        prev = ptr
        while ptr:
            if ptr == node:
                prev.next = ptr.next
                return
            prev = ptr
            ptr = ptr.next

        # list(self.iterate())
        # it seems if the pointer is reset here, it works fine
        nodelist = list(self.iterate())
        print("\n>> nodelist: ", nodelist)
        self._pointer = self._head
        return

    def iterate(self) -> collections.iterable:
        """Iterates the entire list"""
        while self._pointer:
            temp = self._pointer
            nextnode = self._pointer.next
            self._pointer = nextnode
            # bug: self._pointer does not seem to be updated to nextnode
            yield temp
        # restore the pointer to the head
        self._pointer = self._head

