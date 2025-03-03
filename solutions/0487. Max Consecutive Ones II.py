"""
Title: Max Consecutive Ones II
URL: https://leetcode.com/problems/max-consecutive-ones-ii/description/
Difficulty: Medium
Tags: Meta, Google
Topics: Array
Dynamic Programming
Sliding Window

Approach:
- standard sliding window where we expand if number of 0s is less than 2 or contract if number of 0s is 2
- can also solve by treating problem as a 1D version of 827. Making a Large Island but that requires O(n) space
- for follow up, we need to store positions of previous 2 zeroes then keep updating 0 positions as we encounter new numbers

Time Complexity: O(n)
Space Complexity: O(1)



Solution:
"""
from template import *

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        num_zeroes = 0
        l = 0

        # valid state: one or fewer 0s in current sequence
        # invalid state: two 0s in current sequence
        
        for r in range(len(nums)):
            # reached a new element
            if nums[r] == 0:
                num_zeroes += 1
            
            # contract the window if state is invalid
            while num_zeroes == 2:
                if nums[l] == 0:
                    num_zeroes -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res



"""
Question:

Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.

 

Example 1:

Input: nums = [1,0,1,1,0]
Output: 4
Explanation: 
- If we flip the first zero, nums becomes [1,1,1,1,0] and we have 4 consecutive ones.
- If we flip the second zero, nums becomes [1,0,1,1,1] and we have 3 consecutive ones.
The max number of consecutive ones is 4.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 4
Explanation: 
- If we flip the first zero, nums becomes [1,1,1,1,0,1] and we have 4 consecutive ones.
- If we flip the second zero, nums becomes [1,0,1,1,1,1] and we have 4 consecutive ones.
The max number of consecutive ones is 4.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
 

Follow up: What if the input numbers come in one by one as an infinite stream? In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. Could you solve it efficiently?
"""