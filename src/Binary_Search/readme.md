# Overview
There are two types of binary search algorithms:

1. Inclusive at both ends of the range, denoted as '[]'.
2. Inclusive at the left end and exclusive at the right end, denoted as '[)'.

# Both Included
There are two kinds of both included:
1. left strict: 
   - After moving the "left pointer", all elements to the left of the "left pointer" must be smaller than the target value. All elements to the right of the "left pointer" including the element pointed to by the "left pointer" must be equal to or greater than the target value. In other words, the "left pointer" points to the value that is equal to or greater than the target.
   - At the end of the iteration, the value pointed to by the "left pointer" is the target value. When an exact value isn't found, the nearest larger value is selected. If all values are smaller than the target, the "left pointer" moves beyond the right boundary.
2. right strict:
   - After moving the "right pointer", all elements to the right of the "right pointer" must be larger than the target value. All elements to the left of the "right pointer" including the element pointed to by the "right pointer" must be equal to or lower than the target value. In other words, the "right pointer" points to the value that is equal to or lower than the target.
   - At the end of the iteration, the value pointed to by the "right pointer" is the target value. When an exact value isn't found, the nearest lower value is selected. If all values are larger than the target, the "right pointer" moves beyond the left boundary.