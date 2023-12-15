# Overview
There are two types of binary search algorithms:

1. Inclusive at both ends of the range, denoted as '[]'.
2. Inclusive at the left end and exclusive at the right end, denoted as '[)'.

# Essential Considerations for Binary Search
## Both Included
### Overview
When designing a binary search, it's essential to consider four key aspects:

1. end condition
2. update right pointer
3. update condition
4. return pointer

Additionally, it's crucial to be mindful of a specific edge case: When the left and right pointers point to adjacent elements.

Two fundamental statements can greatly simplify the entire code snippet:
1. `middle = (left + right) // 2`: This statement ensures that, in comparison to the right pointer, the middle pointer will be closer to the left pointer.
2. `left = middle + 1`: This statement prevents the code from falling into an infinite loop. Using `left == middle` in the edge case would lead to unintended consequences.

With these considerations, including four aspects, one edge case, and two fixed statements, you can confidently design an effective binary search algorithm. Refer to the accompanying diagram
![both_included_pattern](both_included_pattern.png)
for a visual representation.

Remember the strict mode means the pointer shouldn't miss any possible value or include any impossible value.
There are four scenarios; let's start from end conditions:
1. End condition: `left == right`: End condition: left == right: This means both the left and right pointer must be strict; both left and right shouldn't miss possible values. Based on that:
   1. If `middle = (left + right) // 2`: the middle will be closer to the left pointer, so we must always update the left pointer by `left = middle + 1`. To ensure the left pointer is strict, we can only move the left pointer when `sorted_nums[middle] < target`.
   2. If `middle = (left + right) // 2 + 1`: the middle will be closer to the right pointer, so we must always update the right pointer by `right = middle - 1`. To ensure the right pointer is strict, we can only move the right pointer when `sorted_nums[middle] > target`.
2. End condition: `left <= right`: if we update the middle by `middle = (left + right)`, which means the middle pointer will always be closer to the left pointer, so there is only one way to update the left pointer `left = middle + 1`.
   1. If we update the left pointer by `sorted_nums[middle] < target`, which means it is a left strict method, so, how should we update the right pointer? Imagine the edge case: if we update the right pointer by `right = middle`, the left pointer and right pointer will be overlapped and go into an infinite loop. So, we can only update the right pointer by `right = middle - 1`. We need to return the left pointer.
   2. If we update the left pointer by `sorted_nums[middle] <= target`, which means it is a right strict method, so, how should we update the right pointer? When we use `sorted_nums[middle] <= target` for our left pointer update condition, the right pointer update condition will be `sorted_nums[middle] > target`. Because it is a right strict, the right pointer shouldn't miss any possible value or include any impossible value, so we only update it by `right = middle - 1`, and we will return the right pointer."


### Fuzzy target
It's essential to consider scenarios where the exact target value may not exist. In "left strict" mode, the left pointer tends to point to the larger value, while in "left loose" mode, the right pointer tends to point to a smaller value. Therefore, the "left strict" mode selects the nearest larger value, while the "left loose" mode chooses the nearest lower value. Additionally, the stop condition determines whether the final index surpasses the boundary.

For a more detailed understanding, refer to the following table:
![final index of both included when exact ](both_included_final_index.png)

### Some Variations
#### find minimum in rotated sorted array ii
The question involves a rotated sorted array, indicating it comprises at most two monotonically increasing chunks. Refer to the [code](https://github.com/liushuyu6666/Algorithm_Leetcode_Python/tree/master/src/Find_Minimum_in_Rotated_Sorted_Array_II) for details on "end condition" and "update right pointer."

  
