"""
Title: Max Consecutive Ones III
URL: https://leetcode.com/problems/max-consecutive-ones-iii/description/
Difficulty: Medium
Tags: Meta, Google, LinkedIn, AMazon, Microsoft, Apple
Topics: Array
Binary Search
Sliding Window
Prefix Sum

Approach:
- standard sliding window
- just need to make sure number of zeroes in window is equal to k


Time Complexity: O(n)
Space Complexity: O(1)



Solution:
"""
from template import *

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        num_zeroes = 0
        l = 0

        for r in range(len(nums)):
            # add element to window
            num_zeroes += not nums[r]

            while num_zeroes > k:
                num_zeroes -= not nums[l]
                l += 1
            
            res = max(res, r - l + 1)
        
        return res



"""
Question:

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
"""