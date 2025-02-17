"""
Title: Largest Number At Least Twice of Others
URL: https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/
Difficulty: Easy
Tags: Google, Microsoft, Uber
Topics: Array
Sorting

Approach:
- do a 2 pass solution. q messed me up cause I tried too hard to do a 1 pass
-- avoid trying to keep a second highest number -> that messed me up
- just intialize the highest and res to the first element, and in first loop update accordingly to find the max
- then do one more loop where we make sure every number is 2x less than the highest number


Time Complexity: O(n)
Space Complexity: O(1)



Solution:
"""
from template import *

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        highest = nums[0]
        res = 0
        for i in range(len(nums)):
            if nums[i] > highest:
                highest = nums[i]
                res = i
        
        for i, n in enumerate(nums):
            if highest < 2 * n and highest != n:
                return -1
        
        return res



"""
Question:

You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.

 

Example 1:

Input: nums = [3,6,1,0]
Output: 1
Explanation: 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.
Example 2:

Input: nums = [1,2,3,4]
Output: -1
Explanation: 4 is less than twice the value of 3, so we return -1.
 

Constraints:

2 <= nums.length <= 50
0 <= nums[i] <= 100
The largest element in nums is unique.
"""