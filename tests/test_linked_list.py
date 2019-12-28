from uuid import UUID
import pytest

from src.linkedlist import Node, LinkedList


@pytest.fixture
def node():
    return Node()


@pytest.fixture
def linkedlist():
    return LinkedList()


class TestNode:
    def test_init(self, node):
        assert node is not None

    def test_id(self, node):
        assert node.id is not None
        assert isinstance(node.id, UUID)
        assert len(str(node.id)) == 36

    def test_eq(self, node):
        node2 = Node(node.value)
        assert node2.id != node.id
        assert node2 != node

        node2.id = node.id
        assert node2.id == node.id

        assert node2 == node
        # TODO: why the comparison function failing?

    def test_value(self, node):
        node.value = 42
        assert node.value == 42
        assert node.next is None

        node.value = 43
        assert node.value == 43

    def test_next(self):
        node1 = Node(42)
        node2 = Node(43)

        node1.next = node2

        assert node1.next == node2
        assert node1.next.value == 43


class TestLinkedList:
    def test_init(self, linkedlist):
        assert linkedlist is not None
        assert linkedlist.head is None
        assert linkedlist.last is None

    def test_insert(self, linkedlist, node):
        node.value = 13
        linkedlist.insert(node)
        assert linkedlist.size == 1
        assert linkedlist.head == node
        assert linkedlist.last == node
        assert linkedlist.head.value == node.value
        assert linkedlist.last.value == node.value

    def test_insert_bulk(self, linkedlist):
        nodelist = [Node(_) for _ in range(10)]
        for node in nodelist:
            linkedlist.insert(node)

        assert linkedlist.size == 10
        assert linkedlist.last == nodelist[-1]
        assert linkedlist.head == nodelist[0]

        for index, node in enumerate(linkedlist.iterate()):
            assert node == nodelist[index]

    def test_contains(self, linkedlist):
        nodelist = [Node(_) for _ in range(10)]
        for node in nodelist:
            linkedlist.insert(node)
        for node in nodelist:
            assert node in linkedlist

        assert Node("1337") not in linkedlist

    def test_delete(self, linkedlist, node):
        linkedlist.insert(node)
        linkedlist.delete(node)
        assert linkedlist.head is None
        assert linkedlist.last is None
        assert linkedlist.size == 0
        assert node not in linkedlist

    def test_delete_head(self, linkedlist, node):
        node1, node2, node3 = Node(1), Node(2), Node(3)

        linkedlist.insert(node1)
        linkedlist.insert(node2)
        linkedlist.insert(node3)
        linkedlist.delete(node1)

        assert linkedlist.size == 2
        assert linkedlist.head != node1
        assert linkedlist.head == node2
        assert linkedlist.last == node3
        assert node1 not in linkedlist
        assert node2 in linkedlist
        assert node3 in linkedlist

    def test_delete_tail(self, linkedlist, node):
        node1, node2, node3 = Node(1), Node(2), Node(3)

        linkedlist.insert(node1)
        linkedlist.insert(node2)
        linkedlist.insert(node3)
        linkedlist.delete(node3)

        assert linkedlist.size == 2
        assert linkedlist.head == node1
        assert linkedlist.last != node2
        assert linkedlist.last != node3
        assert node1 not in linkedlist
        assert node2 in linkedlist
        assert node3 in linkedlist

    def test_delete_mid(self, linkedlist, node):
        node1, node2, node3 = Node(1), Node(2), Node(3)

        linkedlist.insert(node1)
        linkedlist.insert(node2)
        linkedlist.insert(node3)
        linkedlist.delete(node2)

        assert linkedlist.size == 2
        assert node1 in linkedlist
        assert node2 not in linkedlist
        assert node3 in linkedlist

    def test_iterate(self, linkedlist, node):
        linkedlist.insert(node)
        linkedlist.insert(Node(10))
        nodelist = [node for node in linkedlist.iterate()]
        assert len(nodelist) == 2

    def test_iterate_delete(self, linkedlist, node):
        new_node = Node(10)
        linkedlist.insert(node)
        linkedlist.insert(new_node)
        linkedlist.delete(new_node)

        nodelist = [node for node in linkedlist.iterate()]
        assert len(nodelist) == 1


