import pytest

from src.queue import Queue


@pytest.fixture
def queue():
    return Queue()


class TestQueue:
    def test_init(self, queue):
        assert queue is not None

    def test_put(self, queue):
        item = "abc"
        queue.put(item)

    def test_get(self, queue):
        queue.put("abc")

        assert queue.get() == "abc"

        with pytest.raises(Exception) as execinfo:
            queue.get()
        assert str(execinfo.value) == "QueueEmptyException"

    def test_size(self, queue):
        queue.put("abc")
        queue.put("def")

        assert queue.size() == 2
        queue.get()
        assert queue.size() == 1
        queue.get()
        assert queue.size() == 0

    def test_max(self):
        queue = Queue(1)
        queue.put("abc")

        with pytest.raises(Exception) as execinfo:
            queue.put("TEST")
        assert str(execinfo.value) == "QueueFullException"

