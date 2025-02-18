"""
Title: Power of Four
URL: https://leetcode.com/problems/power-of-four/description/
Difficulty: Easy
Tags: Google, Amazon, Apple
Topics: Math
Bit Manipulation
Recursion

Approach:
- just keep dividing by 4 and make sure last number is 1
- also some math (w/ log) and bit manipulation gimmicks to solve in O(1)


Time Complexity: O(log(n))
Space Complexity: O(1)



Solution:
"""
from template import *

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0: # avoid divide by 0
            return False

        while n % 4 == 0:
            n //= 4
        
        return n == 1



"""
Question:

Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.

 

Example 1:

Input: n = 16
Output: true
Example 2:

Input: n = 5
Output: false
Example 3:

Input: n = 1
Output: true
 

Constraints:

-231 <= n <= 231 - 1
 

Follow up: Could you solve it without loops/recursion?
"""