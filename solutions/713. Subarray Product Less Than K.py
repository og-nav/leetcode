"""
Title: Subarray Product Less Than K
URL: https://leetcode.com/problems/subarray-product-less-than-k/description/
Difficulty: Medium
Tags: SalesForce, Amazon, Google, Bloomberg, Meta, APple
Topics: Array
Binary Search
Sliding Window
Prefix Sum

Approach:
- standard sliding window
- use res += r - l + 1 to count number of subarrays/substrings
- also consider what if nums[i] is 0 or negative


Time Complexity: O(n)
Space Complexity: O(1)



Solution:
"""
from template import *

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # since it must be strictly less than k
        # and since we know all numbers are positive
        # then if k is equal to 1, then even 1 in nums would be too big
        if k <= 1:
            return 0

        res = 0
        l = 0
        product = 1

        for r in range(len(nums)):
            # add nums[r] to window
            product *= nums[r]

            # while window is invalid
            while product >= k:
                product /= nums[l]
                l += 1
            
            res += r - l + 1
        
        return res



"""
Question:

Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

 

Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Example 2:

Input: nums = [1,2,3], k = 0
Output: 0
 

Constraints:

1 <= nums.length <= 3 * 104
1 <= nums[i] <= 1000
0 <= k <= 106
"""