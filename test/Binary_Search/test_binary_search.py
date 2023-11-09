import random
import unittest
from src.Binary_Search.binary_search import BinarySearch


class TestBinarySearch(unittest.TestCase):

    def test_both_included_left_strict(self):
        binary_search = BinarySearch()

        # when the size is odd
        arr, target, index = [1, 2, 3, 4, 5], 4, 3
        self.assertEqual(binary_search.both_included_left_strict(arr, target), index)

        # when the size is even
        arr, target, index = [1, 2, 3, 4], 3, 2
        self.assertEqual(binary_search.both_included_left_strict(arr, target), index)

        # when an exact value is unavailable, the nearest larger value is chosen.
        arr, target, index = [1, 2, 3, 5, 6], 4, 3
        self.assertEqual(binary_search.both_included_left_strict(arr, target), index)

        # when all elements are smaller than the target, the "left pointer" moves beyond the right boundary.
        arr, target, index = [1, 2, 3, 5, 6], 8, 5
        self.assertEqual(binary_search.both_included_left_strict(arr, target), index)

        # when all elements are larger than the target, the nearest larger value is chosen, which is the first element
        arr, target, index = [11, 12, 13, 15, 16], 1, 0
        self.assertEqual(binary_search.both_included_left_strict(arr, target), index)

    def test_both_included_right_strict(self):
        binary_search = BinarySearch()

        # when the size is odd
        arr, target, index = [1, 2, 3, 4, 5], 4, 3
        self.assertEqual(binary_search.both_included_right_strict(arr, target), index)

        # when the size is even
        arr, target, index = [1, 2, 3, 4], 3, 2
        self.assertEqual(binary_search.both_included_right_strict(arr, target), index)

        # When an exact value is unavailable, the nearest lower value is chosen.
        arr, target, index = [1, 2, 3, 5, 6], 4, 2
        self.assertEqual(binary_search.both_included_right_strict(arr, target), index)

        # when all elements are larger than the target, the "right pointer" moves beyond the left boundary.
        arr, target, index = [11, 12, 13, 15, 16], 4, -1
        self.assertEqual(binary_search.both_included_right_strict(arr, target), index)

        # when all elements are smaller than the target, the nearest lower value is chosen, which is the last element
        arr, target, index = [1, 2, 3, 5, 6], 10, 4
        self.assertEqual(binary_search.both_included_right_strict(arr, target), index)


if __name__ == "__main__":
    unittest.main()

