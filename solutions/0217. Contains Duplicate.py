"""
Title: Contains Duplicate
URL: https://leetcode.com/problems/contains-duplicate/description/
Difficulty: Easy
Tags: NeetCode 150, Grind, Blind 75

Approach:
- just check if length of array is equal to length of the set of the array
- using extra space is OK. there is no O(1) space solution
- might be used as a warm up for Contains Duplicate III


Time Complexity: O(n)
Space Complexity: O(1)



Solution:
"""
from template import *

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))



"""
Question:

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109

"""