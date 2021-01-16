from src.ringbuffer import RingBuffer


class TestRingBuffer:
    def test_init(self):
        rbuf = RingBuffer(10)
        assert rbuf.size == 10

    def test_enqueue(self):
        rbuf = RingBuffer(10)

        value = "0"
        rbuf.enqueue(value)
        assert rbuf.ring[0].value == value
        assert rbuf.write_index == 1

    def test_enqueue_overwrite(self):
        rbuf = RingBuffer(2)

        rbuf.enqueue("1")
        rbuf.enqueue("2")
        rbuf.enqueue("3")
        # this should overwrite the first element

        assert rbuf.ring[0].value == "3"
        assert rbuf.write_index == 1

    def test_dequeue(self):
        rbuf = RingBuffer(10)

        value = "0"
        rbuf.enqueue(value)
        assert rbuf.dequeue() == value
        assert rbuf.read_index == 1

    def test_dequeue_ring(self):
        rbuf = RingBuffer(2)
        rbuf.enqueue("0")
        assert rbuf.dequeue() == "0"
        assert rbuf.read_index == 1

        assert rbuf.dequeue() is None
        assert rbuf.read_index == 0
