import math
from typing import List


#  Please first understand
#  1) both_included_both_strict_left
#  2) both_included_left_strict
#  3) both_included_right_strict
#  Then
#  1) both_included_both_strict_right

class BinarySearch:
    @staticmethod
    def both_included_both_strict_left(sorted_nums: List[int], target: int) -> int:
        left, right = 0, len(sorted_nums) - 1

        while left < right:  # end condition: left == right
            middle = (left + right) // 2
            if sorted_nums[middle] < target:  # left strict
                left = middle + 1
            else:
                right = middle  # assuming edge case

        return left  # left strict

    @staticmethod
    def both_included_both_strict_right(sorted_nums: List[int], target: int) -> int:
        left, right = 0, len(sorted_nums) - 1

        while left < right:  # end condition: left == right
            middle = math.ceil((left + right) / 2)
            if sorted_nums[middle] > target:  # right strict
                right = middle - 1
            else:
                left = middle

        return right  # left strict

    @staticmethod
    def both_included_left_strict(sorted_nums: List[int], target: int) -> int:
        left, right = 0, len(sorted_nums) - 1

        while left <= right:  # end condition: left > right
            middle = (left + right) // 2
            if sorted_nums[middle] < target:  # left strict
                left = middle + 1
            else:
                right = middle - 1

        return left

    @staticmethod
    def both_included_right_strict(sorted_nums: List[int], target: int) -> int:
        left, right = 0, len(sorted_nums) - 1

        while left <= right:  # end condition: left > right
            middle = (left + right) // 2
            if sorted_nums[middle] <= target:  # left loose
                left = middle + 1
            else:
                right = middle - 1

        return right
