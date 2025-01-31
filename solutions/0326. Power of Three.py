"""
Title: Power of Three
URL: https://leetcode.com/problems/power-of-three/description/
Difficulty: Easy
Tags: Bloomberg, Google, Meta, Goldman Sachs, Amazon
Topics: Math
Recursion

Approach:
- I tried doing stuff like checking if divisible by 9 but that doesn't work (ex for 45)
- need to realize that we are limited by int size, so if we check 3 ^ 19, we can see that's the biggest power of
- three we can have
- also need to see that 3 ^ 19 is only divisible by powers of three 
-- 3 ^ 19 = 3 ^ 18 * 3 ^ 1
-- 3 ^ 19 = 3 ^ 15 * 3 ^ 4
-- etc
- so just need to check that n > 0 and that 3 ** 19 % n == 0


Time Complexity: O(1)
Space Complexity: O(1)



Solution:
"""
from template import *

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and not 3 ** 19 % n



"""
Question:

Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

 

Example 1:

Input: n = 27
Output: true
Explanation: 27 = 33
Example 2:

Input: n = 0
Output: false
Explanation: There is no x where 3x = 0.
Example 3:

Input: n = -1
Output: false
Explanation: There is no x where 3x = (-1).
 

Constraints:

-231 <= n <= 231 - 1
 

Follow up: Could you solve it without loops/recursion?
"""