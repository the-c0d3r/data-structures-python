from __future__ import annotations

import uuid
from typing import Any, Optional


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
        return len(self.iterate())

    def get(self, index: int) -> Optional[Node]:
        """
        Returns the node at position
        @param index: the index of the item to acquire from the list
        """
        if index > self.size:
            return None

        count = 0

        ptr = self._head
        while ptr:
            if count == index:
                return ptr
            count += 1
            ptr = ptr.next
        return None

    def pop(self) -> Optional[Node]:
        """Pops the last item in chain and return the node"""
        # Case when it is empty list
        if self._last is None:
            return None

        # Case when it is the last remaining node
        if self._head == self._last:
            node = self._head
            self._head = None
            self._last = None
            self._pointer = None
            return node

        # Case when it is not the only remaining node
        ptr = self._head
        while ptr:
            if ptr.next == self._last:
                break
            ptr = ptr.next
        last_node = ptr.next
        ptr.next = None
        self._last = ptr
        return last_node

    def insert(self, node: Node) -> None:
        """Inserts the node into the list"""
        # empty linked list, point all three pointers to node
        if self._head is None:
            self._head = node
            self._last = node
            self._pointer = node
        else:
            # update old _last node's next to new node, update _last to new node
            self._last.next = node
            self._last = node

    def delete(self, node: Node) -> None:
        """Deletes the given node from list"""
        # Case when node does not exist
        if node not in self:
            return

        # Case when node is the only node
        if self.size == 1:
            self._head = None
            self._last = None
            self._pointer = None
            return

        # Case when node is head
        if node == self._head:
            self._head = self._head.next
            self._pointer = self._head
            return

        # Case when node is last
        if node == self._last:
            # iterate to exhaust all the nodes and get the last node before
            ptr = self._head
            prev = None
            while ptr.next:
                prev = ptr
                ptr = ptr.next
            self._last = prev
            prev.next = None
            return

        # Case when node is in the middle
        ptr = self._head
        prev = None
        while ptr:
            prev = ptr
            ptr = ptr.next
            if ptr == node:
                prev.next = ptr.next
                return

    def iterate(self) -> [Optional[Node]]:
        """
        Note: if generator approach is used, one needs to make sure self._pointer
        is reset. This will not happen in condition checks like Node "in" self. In
        this case, when node exists, it will just return, without the resetting of
        self._pointer being executed
        """
        nodes = []
        while self._pointer:
            nodes.append(self._pointer)
            self._pointer = self._pointer.next

        self._pointer = self._head
        return nodes
