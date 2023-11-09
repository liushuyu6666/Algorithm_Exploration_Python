from typing import List


class BinarySearch:
    @staticmethod
    def both_included_left_strict(sorted_nums: List[int], target: int) -> int:
        left, right = 0, len(sorted_nums) - 1

        while left <= right:
            middle = (left + right) // 2
            # The target value always resides to the right of the left pointer because sorted_nums[middle] != target.
            # The target value always resides to the left of the right pointer or at the position pointed by the middle.
            if sorted_nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return left

    @staticmethod
    def both_included_right_strict(sorted_nums: List[int], target: int) -> int:
        left, right = 0, len(sorted_nums) - 1

        while left <= right:
            middle = (left + right) // 2
            # The target value always resides to the left of the right pointer because sorted_nums[middle] != target.
            # The target value always resides to the right of the left pointer or at the position pointed by the middle.
            if sorted_nums[middle] <= target:
                left = middle + 1
            else:
                right = middle - 1

        return right
