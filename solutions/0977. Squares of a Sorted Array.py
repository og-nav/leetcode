"""
Title: Squares of a Sorted Array
URL: https://leetcode.com/problems/squares-of-a-sorted-array/description/
Difficulty: Easy
Tags: Grind, Uber, Meta, Google, Amazon, Bloomberg, Apple, Adobe, Walmart, Yahoo, Microsoft
Topics: String, Stack, etc

Approach:
- two pointers from each side of nums
- just append the square of the value whose absolute value is bigger
- also consider using a deque to save the extra step of reversing at the end


Time Complexity: O(n)
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        l, r = 0, len(nums) - 1
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res.append(nums[l] ** 2)
                l += 1
            else:
                res.append(nums[r] ** 2)
                r -= 1
        
        return res[::-1]



"""
Question:

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
 

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
"""