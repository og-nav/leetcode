"""
Title: Identify the Largest Outlier in an Array
URL: https://leetcode.com/problems/identify-the-largest-outlier-in-an-array/description/
Difficulty: Medium
Tags: Amazon, Meta, Google
Topics: Array
Hash Table
Counting
Enumeration

Approach:
- use the formula to isolate the outlier: outlier = total_sum - 2 * n
- and we iterate through nums and operate under the assumption that the current number is potentially the sum of all the special numbers
- an outlier cannot belong to the special numbers, so if we potentially find it, we must ensure that it is not equal to n because n is now the sum of all the special numbers
-- then we can also check if it occurs multiple times, and if so it is valid


Time Complexity: O(n)
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        # sum of nums = 2 * sum_special + outlier
        total_sum = sum(nums)
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1

        res = float('-inf')
        for n in nums:
            # we operate under the assumption that the current number is potentially the sum of all the special numbers
            potential_outlier = total_sum - 2 * n

            if potential_outlier in counts:
                if potential_outlier != n or counts[n] > 1:
                    res = max(res, potential_outlier)
        
        return res



"""
Question:

You are given an integer array nums. This array contains n elements, where exactly n - 2 elements are special numbers. One of the remaining two elements is the sum of these special numbers, and the other is an outlier.

An outlier is defined as a number that is neither one of the original special numbers nor the element representing the sum of those numbers.

Note that special numbers, the sum element, and the outlier must have distinct indices, but may share the same value.

Return the largest potential outlier in nums.

 

Example 1:

Input: nums = [2,3,5,10]

Output: 10

Explanation:

The special numbers could be 2 and 3, thus making their sum 5 and the outlier 10.

Example 2:

Input: nums = [-2,-1,-3,-6,4]

Output: 4

Explanation:

The special numbers could be -2, -1, and -3, thus making their sum -6 and the outlier 4.

Example 3:

Input: nums = [1,1,1,1,1,5,5]

Output: 5

Explanation:

The special numbers could be 1, 1, 1, 1, and 1, thus making their sum 5 and the other 5 as the outlier.

 

Constraints:

3 <= nums.length <= 105
-1000 <= nums[i] <= 1000
The input is generated such that at least one potential outlier exists in nums.
"""