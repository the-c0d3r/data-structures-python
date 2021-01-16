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

    def enqueue(self, value: Any) -> None:
        """enqueue the value into the ring buffer"""
        self.ring[self.write_index].value = value
        self.write_index = (self.write_index + 1) % self.size

    def dequeue(self) -> Any:
        """dequeue the value from the ring buffer"""
        value = self.ring[self.read_index].value
        self.ring[self.read_index].value = SENTINEL
        self.read_index = (self.read_index + 1) % self.size

        return value
