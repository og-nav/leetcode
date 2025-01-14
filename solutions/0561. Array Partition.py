"""
Title: Array Partition
URL: https://leetcode.com/problems/array-partition/description/
Difficulty: Easy
Tags: Amazon, Bloomberg, Google, Meta, Apple
Topics: Array
Greedy
Sorting
Counting Sort

Approach:
- need to make the realization you need to sort and go pairwise
- since we want to maximize final sum, we want to make sure all small numbers get sacrificed with other small numbers
- and that big numbers are only sacrificed by big numbers
- so we sort, and then iterate over each pair and add the min of nums[i] and nums[i - 1] to the result


Time Complexity: O(nlog(n))
Space Complexity: O(n) -> python uses Timsort so it uses O(n) space



Solution:
"""
from template import *

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        
        for i in range(1, len(nums), 2):
            res += min(nums[i], nums[i - 1])
        
        return res



"""
Question:

Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

 

Example 1:

Input: nums = [1,4,3,2]
Output: 4
Explanation: All possible pairings (ignoring the ordering of elements) are:
1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
So the maximum possible sum is 4.
Example 2:

Input: nums = [6,2,6,5,1,2]
Output: 9
Explanation: The optimal pairing is (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9.
 

Constraints:

1 <= n <= 104
nums.length == 2 * n
-104 <= nums[i] <= 104
"""