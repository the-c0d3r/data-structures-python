from typing import Any, List

SENTINEL = None


class Element:
    def __init__(self, value: Any) -> None:
        self.used = False
        self.value = value


class RingBuffer:
    def __init__(self, size: int) -> None:
        self.size: int = size
        self.read_index: int = 0
        self.write_index: int = 0
        self.ring: List[Element] = [Element(None)] * self.size

    def incr_read_index(self):
        """increment the read index"""
        self.read_index += 1
        if self.read_index == self.size:
            self.read_index = 0

    def incr_write_index(self):
        """increment the write index"""
        self.write_index += 1
        if self.write_index == self.size:
            self.write_index = 0

    def enqueue(self, value: Any) -> None:
        """enqueue the value into the ring buffer"""
        self.ring[self.write_index].value = value
        self.incr_write_index()

    def dequeue(self) -> Any:
        """dequeue the value from the ring buffer"""
        value = self.ring[self.read_index].value
        self.ring[self.read_index].value = SENTINEL
        self.incr_read_index()

        return value
