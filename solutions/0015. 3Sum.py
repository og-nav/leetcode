"""
Title: 3Sum
URL: https://leetcode.com/problems/3sum/description/
Difficulty: Medium
Tags: NeetCode 150, Grind, Blind 75, Meta, Google, Amazon, Microsoft, Bloomberg, Popular
Topics: Array
Two Pointers
Sorting

Approach:
- sort then fix one variable using outer for loop then do 2 sum using an inner for loop
- use set for res to avoid duplicates
- this answer runs very slow despite being the same time complexity as the optimal answer
- because set look up takes a long time compared to direct memory access
- look up other people's answer when doing interview prep

Time Complexity: O(n ^ 2)
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        
        for i in range(len(nums)):
            complement = defaultdict(int)
            for j in range(i + 1, len(nums)):
                if nums[j] in complement:
                    res.add((nums[i], nums[j], complement[nums[j]]))
                else:
                    complement[0 - nums[i] - nums[j]] = nums[j]
        
        return list(res)



"""
Question:

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""