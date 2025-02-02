"""
Title: Check if Array is Sorted and Rotated
URL: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/
Difficulty: Easy
Tags: Google, Amazon, Bloomberg, Adobe, Meta, Microsoft, Uber, Yahoo, Apple
Topics: Array

Approach:
- utilize property of sorted array
-- if the array started out sorted but was rotated, there will be at most 1 "dip" between adjacent numbers
-- then just need to check last element against the first element as well
- for example, [2, 1, 3, 4] -> 2 dips to 1 and then 4 dips to 2
- in [3, 4, 5, 1, 2] -> 5 dips to 1 but no more dips after that
- so number of dips must be 1 or less (would be 0 if the array is already sorted with no rotation)


Time Complexity: O(n)
Space Complexity: O(1)



Solution:
"""
from template import *

class Solution:
    def check(self, nums: List[int]) -> bool:
        dips = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                dips += 1
        
        if nums[-1] > nums[0]:
            dips += 1
        
        return not dips > 1



"""
Question:

Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].
Example 2:

Input: nums = [2,1,3,4]
Output: false
Explanation: There is no sorted array once rotated that can make nums.
Example 3:

Input: nums = [1,2,3]
Output: true
Explanation: [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100

"""