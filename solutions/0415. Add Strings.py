"""
Title: Add Strings
URL: https://leetcode.com/problems/add-strings/description/
Difficulty: Easy
Tags: Meta, TikTok, Google, Amazon, Microsoft, Bloomberg, Apple
Topics: Math
String
Simulation

Approach:
- we can just go digit by digit
- and make sure to account for carry
- use special two pointer technique so that you don't need multiple if/while loops afterward to handle if they
-- are different lengths


Time Complexity: O(max(m, n)) -> where m is the length of num1 and n is the length of num2
Space Complexity: O(max(m, n))



Solution:
"""
from template import *

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0

        while i >= 0 or j >= 0:
            n = ord(num1[i]) - ord('0') if i >= 0 else 0  # in case int(num1[i]) is not allowed
            m = ord(num2[j]) - ord('0') if j >= 0 else 0
            
            digit = (n + m + carry) % 10
            carry = (n + m + carry) // 10
            res.append(str(digit))

            i -= 1
            j -= 1
        
        if carry:
            res.append('1')
        
        return "".join(res[::-1])



"""
Question:

Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"
 

Constraints:

1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.
"""