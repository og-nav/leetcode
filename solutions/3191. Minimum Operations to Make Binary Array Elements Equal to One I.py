"""
Title: Minimum Operations to Make Binary Array Elements Equal to One I
URL: https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/description/
Difficulty: Medium
Tags: Amazon, Uber
Topics: Array
Bit Manipulation
Queue
Sliding Window
Prefix Sum

Approach:
- key insight is that if nums[0] is 0, then the only move we can make is to flip the first 3 bits
-- then going right, apply that same logic to nums[1]
-- continue for the entire array
- then just check if any of the last 3 numbers are 0, and if so, it is impossible
- so it is basically like a greedy solution


Time Complexity: O(n)
Space Complexity: O(1) -> only if modifying nums. if we need to make a copy, then it's O(n)



Solution:
"""
from template import *

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        nums_copy = nums[::]
        for i in range(len(nums) - 2):
            if nums_copy[i] == 0:
                for j in range(i, i + 3):
                    nums_copy[j] = int(not nums_copy[j])
                
                res += 1
        
        for i in range(len(nums_copy) - 2, len(nums_copy)):
            if nums_copy[i] == 0:
                return -1
        
        return res



"""
Question:

You are given a binary array nums.

You can do the following operation on the array any number of times (possibly zero):

Choose any 3 consecutive elements from the array and flip all of them.
Flipping an element means changing its value from 0 to 1, and from 1 to 0.

Return the minimum number of operations required to make all elements in nums equal to 1. If it is impossible, return -1.

 

Example 1:

Input: nums = [0,1,1,1,0,0]

Output: 3

Explanation:
We can do the following operations:

Choose the elements at indices 0, 1 and 2. The resulting array is nums = [1,0,0,1,0,0].
Choose the elements at indices 1, 2 and 3. The resulting array is nums = [1,1,1,0,0,0].
Choose the elements at indices 3, 4 and 5. The resulting array is nums = [1,1,1,1,1,1].
Example 2:

Input: nums = [0,1,1,1]

Output: -1

Explanation:
It is impossible to make all elements equal to 1.

 

Constraints:

3 <= nums.length <= 105
0 <= nums[i] <= 1
"""