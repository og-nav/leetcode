"""
Title: Monotonic Array
URL: https://leetcode.com/problems/monotonic-array/description/
Difficulty: Easy
Tags: Meta, Amazon, Google
Topics: Array

Approach:
- use for-else to check if decreasing then check if increasing otherwise return false


Time Complexity: O(n)
Space Complexity: O(1)



Solution:
"""
from template import *

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # check if decreasing
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                break
        else:
            return True
        
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                break
        else:
            return True
        
        return False



"""
Question:

An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

 

Example 1:

Input: nums = [1,2,2,3]
Output: true
Example 2:

Input: nums = [6,5,4,4]
Output: true
Example 3:

Input: nums = [1,3,2]
Output: false
 

Constraints:

1 <= nums.length <= 105
-105 <= nums[i] <= 105
"""