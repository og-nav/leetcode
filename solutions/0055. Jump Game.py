"""
Title: Jump Game
URL: https://leetcode.com/problems/jump-game/description/
Difficulty: Medium
Tags: NeetCode 150, Grind, Blind 75, Amazon, Google, Microsoft, Meta, Apple, Popular
Topics: Array
Dynamic Programming
Greedy

Approach:
- just need to see if we can reach the end, don't need the shortest path
- so just denote a safe index
- and any time we can surpass it, update it to the current index
- then just return if it equals 0 (we made it to the beginning)


Time Complexity: O(n)
Space Complexity: O(1)



Solution:
"""
from template import *

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        safe = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= safe:
                safe = i
        
        return safe == 0



"""
Question:

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
"""