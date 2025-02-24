"""
Title: Max Consecutive Ones
URL: https://leetcode.com/problems/max-consecutive-ones/description/
Difficulty: Easy
Tags: Google, Amazon, Meta, Microsoft, Bloomberg
Topics: Array

Approach:
- just keep a current count of consecutive ones and update res accordingly


Time Complexity: O(n)
Space Complexity: O(1)



Solution:
"""
from template import *

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        curr = 0

        for n in nums:
            if n == 0:
                res = max(res, curr)
                curr = 0
            else:
                curr += 1
        
        res = max(res, curr)
        return res



"""
Question:

Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""