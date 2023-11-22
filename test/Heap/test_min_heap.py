import unittest

from src.Heap.min_heap import MinHeap


class TestHeap(unittest.TestCase):

    def test_min_heap_characteristics(self, min_heap: MinHeap):
        # test one of its characteristics: the parent node should be smaller than any of its children.
        curr_index = 1
        while curr_index <= min_heap.size // 2:
            left_child = curr_index * 2
            right_child = curr_index * 2 + 1 if curr_index * 2 + 1 <= min_heap.size else left_child
            self.assertLess(min_heap.heap[curr_index], min_heap.heap[left_child],
                            msg=f"{curr_index} should be smaller than its left child!")
            self.assertLess(min_heap.heap[curr_index], min_heap.heap[right_child],
                            msg=f"{curr_index} should be smaller than its right child!")
            curr_index += 1

    def test_min_heap(self):
        nums = [3, 6, 9, 5, 6, 4]
        min_heap = MinHeap(nums)

        # test its size
        self.assertEqual(min_heap.size, 6)
        self.test_min_heap_characteristics(min_heap)

        # test its push function
        min_heap.push(1)
        self.assertEqual(min_heap.top(), 1)
        self.test_min_heap_characteristics(min_heap)

        min_heap.push(2)
        self.assertEqual(min_heap.top(), 1)
        self.test_min_heap_characteristics(min_heap)

        # test its pop function
        min_heap.pop()
        self.assertEqual(min_heap.top(), 2)
        self.test_min_heap_characteristics(min_heap)

        min_heap.pop()
        self.assertEqual(min_heap.top(), 3)
        self.test_min_heap_characteristics(min_heap)

        min_heap.push(1)
        self.assertEqual(min_heap.top(), 1)
        self.test_min_heap_characteristics(min_heap)


if __name__ == "__main__":
    unittest.main()
