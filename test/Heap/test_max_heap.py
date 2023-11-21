import unittest
from typing import List

from src.Heap.max_heap import MaxHeap


class TestHeap(unittest.TestCase):

    def test_max_heap_characteristics(self, max_heap: MaxHeap):
        # test one of its characteristics: the parent node should be larger than any of its children.
        curr_index = 1
        while curr_index <= max_heap.size // 2:
            left_child = curr_index * 2
            right_child = curr_index * 2 + 1 if curr_index * 2 + 1 <= max_heap.size else left_child
            self.assertGreater(max_heap.heap[curr_index], max_heap.heap[left_child],
                               msg=f"{curr_index} should be greater than its left child!")
            self.assertGreater(max_heap.heap[curr_index], max_heap.heap[right_child],
                               msg=f"{curr_index} should be greater than its right child!")
            curr_index += 1

    def test_max_heap(self):
        nums = [3, 2, 1, 5, 6, 4]
        max_heap = MaxHeap(nums)

        # test its size
        self.assertEqual(max_heap.size, 6)
        self.test_max_heap_characteristics(max_heap)

        # test its push function
        max_heap.push(9)
        self.assertEqual(max_heap.top(), 9)
        self.test_max_heap_characteristics(max_heap)

        max_heap.push(8)
        self.assertEqual(max_heap.top(), 9)
        self.test_max_heap_characteristics(max_heap)

        # test its pop function
        max_heap.pop()
        self.assertEqual(max_heap.top(), 8)
        self.test_max_heap_characteristics(max_heap)

        max_heap.pop()
        self.assertEqual(max_heap.top(), 6)
        self.test_max_heap_characteristics(max_heap)


if __name__ == "__main__":
    unittest.main()
