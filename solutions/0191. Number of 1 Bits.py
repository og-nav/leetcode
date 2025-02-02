"""
Title: Number of 1 Bits
URL: https://leetcode.com/problems/number-of-1-bits/description/
Difficulty: Easy
Tags: NeetCode 150, Grind, Blind 75, Google, Apple, Amazon, Microsoft, Meta, Bloomberg, Adobe, Uber
Topics: Divide and Conquer
Bit Manipulation

Approach:
- append to n % 2 to res and shift right one bit
- I think my actual answer is the answer to the follow up


Time Complexity: O(log(n)) -> might be O(1) since there are only 32 bits so it runs at most 32 times
Space Complexity: O(1)



Solution:
"""
from template import *

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n > 0:
            res += n % 2
            n >>= 1
        
        return res



"""
Question:

Given a positive integer n, write a function that returns the number of 
set bits
 in its binary representation (also known as the Hamming weight).

 

Example 1:

Input: n = 11

Output: 3

Explanation:

The input binary string 1011 has a total of three set bits.

Example 2:

Input: n = 128

Output: 1

Explanation:

The input binary string 10000000 has a total of one set bit.

Example 3:

Input: n = 2147483645

Output: 30

Explanation:

The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

 

Constraints:

1 <= n <= 231 - 1
 

Follow up: If this function is called many times, how would you optimize it?
"""