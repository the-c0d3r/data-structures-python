from typing import Optional

from linkedlist import LinkedList
from linkedlist import Node


class DoubleLinkedNode(Node):
    _prev = None

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, value):
        self._prev = value


class DoubleLinkedList(LinkedList):

    def insert(self, node: DoubleLinkedNode) -> None:
        """Inserts the node into the list"""
        if self._head is None:
            self._head = node
            self._last = node
            self._pointer = node
        else:
            self._last.next = node
            node.prev = self._last
            self._last = node

    def delete(self, node: DoubleLinkedNode) -> None:
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
            self._head.prev = None
            self._pointer = self._head
            return

        # Case when node is last
        if node == self._last:
            # iterate to exhaust all the nodes and get the last node before
            self._last = self._last.prev
            self._last.next = None

        # Case when node is in the middle
        ptr = self._head
        while ptr.next:
            ptr = ptr.next
            if ptr == node:
                ptr.prev.next = ptr.next
                ptr.next.prev = ptr.prev
                return

    def pop(self) -> Optional[DoubleLinkedNode]:
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
        node = self._last
        self._last = self._last.prev
        self._last.next = None

        return node
