"""
Title: Range Sum Query - Immutable
URL: https://leetcode.com/problems/range-sum-query-immutable/description/
Difficulty: Easy
Tags: Google, Meta, Amazon, Microsoft
Topics: Array
Design
Prefix Sum

Approach:
- prefix sum 
- make sure to add an extra dummy 0 at the beginning for the prefix sum
-- this allows us from having to use a conditional check of whether left is 0 or not


Time Complexity: O(n) -> each query is O(1) so O(n) for n queries
Space Complexity: O(n)



Solution:
"""
from template import *

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0 for _ in range(len(nums) + 1)]
        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i]
        
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)



"""
Question:

Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

Example 1:

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
 

Constraints:

1 <= nums.length <= 104
-105 <= nums[i] <= 105
0 <= left <= right < nums.length
At most 104 calls will be made to sumRange.
"""