"""
Title: Longest Strictly Increasing or Strictly Decreasing Subarray
URL: https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/description/
Difficulty: Easy
Tags: Meta, Bloomberg, Google, Microsoft
Topics: Array

Approach:
- just need two variables keeping track of the current longest increasing streak and decreasing streak
- just make sure to reset to 1 instead of 0


Time Complexity: O(n)
Space Complexity: O(1)



Solution:
"""
from template import *

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increasing = 1
        decreasing = 1
        res = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                increasing += 1
            else:
                increasing = 1
            
            if nums[i] < nums[i - 1]:
                decreasing += 1
            else:
                decreasing = 1
            
            res = max(res, increasing, decreasing)
        
        return res



"""
Question:

You are given an array of integers nums. Return the length of the longest 
subarray
 of nums which is either 
strictly increasing
 or 
strictly decreasing
.

 

Example 1:

Input: nums = [1,4,3,3,2]

Output: 2

Explanation:

The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].

The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].

Hence, we return 2.

Example 2:

Input: nums = [3,3,3,3]

Output: 1

Explanation:

The strictly increasing subarrays of nums are [3], [3], [3], and [3].

The strictly decreasing subarrays of nums are [3], [3], [3], and [3].

Hence, we return 1.

Example 3:

Input: nums = [3,2,1]

Output: 3

Explanation:

The strictly increasing subarrays of nums are [3], [2], and [1].

The strictly decreasing subarrays of nums are [3], [2], [1], [3,2], [2,1], and [3,2,1].

Hence, we return 3.

 

Constraints:

1 <= nums.length <= 50
1 <= nums[i] <= 50
"""