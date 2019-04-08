from src.stack import Stack

import pytest

@pytest.fixture
def stack():
    return Stack()


class TestStack:
    def test_init(self, stack):
        assert stack is not None

    def test_push(self, stack):
        for num in range(1000):
            stack.push(num)
        assert stack.size() == 1000

    def test_pop(self, stack):
        # test popping the stack
        stack.push(1)
        stack.push(2)
        stack.push(3)

        assert stack._index == 3

        assert stack.pop() == 3
        assert stack.size() == 2
        assert stack.stack == [1, 2]

        assert stack.pop() == 2
        assert stack.size() == 1
        assert stack.stack == [1]

        assert stack.pop() == 1
        assert stack.size() == 0
        assert stack.stack == []

    def test_size(self):
        # test if the size is being enforced
        stack = Stack(size = 10)
        for num in range(1000):
            stack.push(num)
        assert stack.size() == 10
        assert stack.stack == [_ for _ in range(10)]
