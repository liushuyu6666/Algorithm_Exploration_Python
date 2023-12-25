import unittest
from src.Iterator.ring_buffer import MyRingBuffer

class TestRingBuffer(unittest.TestCase):
    #  run automatically before each case
    def setUp(self):
        print("set up the ring buffer...")
        self.ring_buffer = MyRingBuffer(5)

        # set up ring buffer
        for i in range(5):
            self.ring_buffer.add(i + 1)

    def next_iteration_3(self):
        print("iterate the first three elements")

        # Test the __next__ method to ensure correct iteration
        self.assertEqual(next(self.ring_buffer), 1)
        self.assertEqual(next(self.ring_buffer), 2)
        self.assertEqual(next(self.ring_buffer), 3)

    def next_iteration_5(self):
        print("iterate the first five elements")

        # Test the __next__ method to ensure correct iteration
        self.assertEqual(next(self.ring_buffer), 1)
        self.assertEqual(next(self.ring_buffer), 2)
        self.assertEqual(next(self.ring_buffer), 3)
        self.assertEqual(next(self.ring_buffer), 4)
        self.assertEqual(next(self.ring_buffer), 5)

    def test_iterator_creation(self):
        print("iterator creation")

        self.assertEqual(iter(self.ring_buffer), self.ring_buffer)

    def test_next_method(self):
        self.next_iteration_3()

    def test_next_loop(self):
        self.next_iteration_3()

        print("test next loop")

        self.ring_buffer.add(6)
        self.ring_buffer.add(7)
        self.ring_buffer.add(8)

        # Test the __next__ method to ensure correct iteration
        self.assertEqual(next(self.ring_buffer), 4)
        self.assertEqual(next(self.ring_buffer), 5)
        self.assertEqual(next(self.ring_buffer), 6)
        self.assertEqual(next(self.ring_buffer), 7)

    def test_next_loop_overflow(self):
        self.next_iteration_5()

        self.ring_buffer.add(6)

        next(self.ring_buffer)

        with self.assertRaises(StopIteration):
            next(self.ring_buffer)


if __name__ == '__main__':
    unittest.main()

