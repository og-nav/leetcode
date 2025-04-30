"""
Title: Find Numbers with Even Numbers of Digits
URL: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/
Difficulty: Easy
Tags: Microsoft, Google
Topics: Array
Math

Approach:
- brute force w/ // 


Time Complexity: O(nlog(m)) -> n nums in nums and log(m) to count num digits
Space Complexity: O(1)



Solution:
"""
from template import *

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            num_digits = 0
            while n >= 1:
                n //= 10
                num_digits += 1
            
            res += num_digits % 2 == 0
        
        return res



"""
Question:

Given an array nums of integers, return how many of them contain an even number of digits.

 

Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.
Example 2:

Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.
 

Constraints:

1 <= nums.length <= 500
1 <= nums[i] <= 105
"""