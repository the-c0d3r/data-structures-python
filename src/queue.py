from typing import Any


class Queue:
    def __init__(self, max: int = 0) -> None:
        self._queue = []
        self._max = max

    def put(self, item: Any) -> None:
        """Put the item to queue"""
        if self._max and self.size() >= self._max:
            raise Exception("QueueFullException")
        self._queue.append(item)

    def get(self) -> Any:
        """Return the item from queue"""
        if self.size() == 0:
            raise Exception("QueueEmptyException")
        return self._queue.pop(0)

    def size(self) -> int:
        """Get the size of the queue"""
        return len(self._queue)
