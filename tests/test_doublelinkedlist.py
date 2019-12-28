import pytest

from src.doublelinkedlist import DoubleLinkedNode, DoubleLinkedList


@pytest.fixture
def node():
    return DoubleLinkedNode()


@pytest.fixture
def doublelinkedlist():
    return DoubleLinkedList()


class TestNode:
    def test_prev(self):
        node1 = DoubleLinkedNode(42)
        node2 = DoubleLinkedNode(43)

        node1.next = node2
        node2.prev = node1

        assert node1.next == node2
        assert node2.prev == node1
        assert node2.prev.value == 42


class TestDoubleLinkedList:
    def test_init(self, doublelinkedlist):
        assert doublelinkedlist is not None
        assert doublelinkedlist.head is None
        assert doublelinkedlist.last is None

    def test_insert(self, doublelinkedlist, node):
        node.value = 42
        doublelinkedlist.insert(node)
        assert doublelinkedlist.size == 1
        assert doublelinkedlist.head == node
        assert doublelinkedlist.last == node
        assert doublelinkedlist.head.value == node.value
        assert doublelinkedlist.last.value == node.value

    def test_insert_bulk(self, doublelinkedlist):
        nodelist = [DoubleLinkedNode(_) for _ in range(10)]
        for node in nodelist:
            doublelinkedlist.insert(node)

        assert doublelinkedlist.size == 10
        assert doublelinkedlist.last == nodelist[-1]
        assert doublelinkedlist.head == nodelist[0]

        assert doublelinkedlist.last.prev == nodelist[-2]

    def test_get(self, doublelinkedlist):
        node1 = DoubleLinkedNode(1)
        node2 = DoubleLinkedNode(2)
        node3 = DoubleLinkedNode(3)
        doublelinkedlist.insert(node1)
        doublelinkedlist.insert(node2)
        doublelinkedlist.insert(node3)

        assert doublelinkedlist.get(0) == node1
        assert doublelinkedlist.get(1) == node2
        assert doublelinkedlist.get(2) == node3
        assert doublelinkedlist.get(1000) is None

    def test_pop(self, doublelinkedlist):
        node1 = DoubleLinkedNode(1)
        node2 = DoubleLinkedNode(2)
        node3 = DoubleLinkedNode(3)
        doublelinkedlist.insert(node1)
        doublelinkedlist.insert(node2)
        doublelinkedlist.insert(node3)

        assert doublelinkedlist.pop() == node3
        assert doublelinkedlist.size == 2
        assert doublelinkedlist.pop() == node2
        assert doublelinkedlist.size == 1
        assert doublelinkedlist.pop() == node1
        assert doublelinkedlist.size == 0
        assert doublelinkedlist.pop() is None

    def test_delete_head(self, doublelinkedlist):
        node1 = DoubleLinkedNode(1)
        node2 = DoubleLinkedNode(2)
        node3 = DoubleLinkedNode(3)

        doublelinkedlist.insert(node1)
        doublelinkedlist.insert(node2)
        doublelinkedlist.insert(node3)

        assert doublelinkedlist.size == 3

        doublelinkedlist.delete(node1)
        assert doublelinkedlist.size == 2
        assert doublelinkedlist.head.next == node3
        assert doublelinkedlist.last.prev == node2

    def test_delete_mid(self, doublelinkedlist):
        node1 = DoubleLinkedNode(1)
        node2 = DoubleLinkedNode(2)
        node3 = DoubleLinkedNode(3)

        doublelinkedlist.insert(node1)
        doublelinkedlist.insert(node2)
        doublelinkedlist.insert(node3)

        assert doublelinkedlist.size == 3

        doublelinkedlist.delete(node2)

        assert doublelinkedlist.size == 2
        assert doublelinkedlist.head.next == node3
        assert doublelinkedlist.last.prev == node1

    def test_delete_tail(self, doublelinkedlist):
        node1 = DoubleLinkedNode(1)
        node2 = DoubleLinkedNode(2)
        node3 = DoubleLinkedNode(3)

        doublelinkedlist.insert(node1)
        doublelinkedlist.insert(node2)
        doublelinkedlist.insert(node3)

        assert doublelinkedlist.size == 3

        doublelinkedlist.delete(node3)
        assert doublelinkedlist.size == 2
        assert doublelinkedlist.head.next == node2
        assert doublelinkedlist.last.prev == node1


