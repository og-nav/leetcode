"""
Title: 1. Two Sum
URL: https://leetcode.com/problems/two-sum/


Approach:
- create a hashmap that stores the complement (target - current number) as the key and the index as the value. 
- iterate through the array and if there is a match, return the current index and the hashmap index.
- make sure to use enumerate to simplify code.


Time Complexity: O(n)
Space Complexity: O(n)

Solution:
"""
from template import *
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        
        for i, n in enumerate(nums):
            if n in complement:
                return [i, complement[n]]
            complement[target - n] = i


"""
Question:

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""