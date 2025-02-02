"""
Title: Fibonacci Number
URL: https://leetcode.com/problems/fibonacci-number/description/
Difficulty: Easy
Tags: Amazon, Microsoft, Google, Meta, Apple, Nvidia, Adobe, Bloomberg, Uber
Topics: Math
Dynamic Programming
Recursion
Memoization

Approach:
- just follow the formula starting with a = 0, b = 1, and iterating thru n
- don't try to get smart by doing 1, 1 and doing n - 2 or stuff like that


Time Complexity: O(n)
Space Complexity: O(1)



Solution:
"""
from template import *

class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            c = a + b
            a = b
            b = c
        
        return a



"""
Question:

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

 

Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 

Constraints:

0 <= n <= 30
"""