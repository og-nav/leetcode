"""
Title: Most Frequent Even Element
URL: https://leetcode.com/problems/most-frequent-even-element/description/
Difficulty: Easy
Tags: Google
Topics: Array
Hash Table
Counting

Approach:
- use counter and update result while adding to counter
- need to separate cases where count is > vs when ==


Time Complexity: O(n)
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        highest_count = 0
        res = -1

        for n in nums:
            counter[n] += 1
            if n % 2 == 0:
                if counter[n] > highest_count:
                    res = n
                    highest_count = counter[n]
                elif counter[n] == highest_count:
                    res = min(res, n)
        
        return res



"""
Question:

Given an integer array nums, return the most frequent even element.

If there is a tie, return the smallest one. If there is no such element, return -1.

 

Example 1:

Input: nums = [0,1,2,2,4,4,1]
Output: 2
Explanation:
The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
We return the smallest one, which is 2.
Example 2:

Input: nums = [4,4,4,9,2,4]
Output: 4
Explanation: 4 is the even element appears the most.
Example 3:

Input: nums = [29,47,21,41,13,37,25,7]
Output: -1
Explanation: There is no even element.
 

Constraints:

1 <= nums.length <= 2000
0 <= nums[i] <= 105
"""