"""
Title: Permutations
URL: https://leetcode.com/problems/permutations/description/
Difficulty: Medium
Tags: NeetCode 150, Grind, Google, Amazon, Meta, Microsoft, Adobe
Topics: Array
Backtracking

Approach:
- backtracking
- use array instead of a set


Time Complexity: O(n!)
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(curr, available):
            if len(curr) == len(nums):
                res.append(curr[::])
                return
            
            for i in range(len(available)):
                curr.append(available[i])
                backtrack(curr, available[: i] + available[i + 1::])
                curr.pop()
        
        backtrack([], nums)
        return res



"""
Question:

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""