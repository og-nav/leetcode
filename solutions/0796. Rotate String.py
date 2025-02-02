"""
Title: Rotate String
URL: https://leetcode.com/problems/rotate-string/description/
Difficulty: Easy
Tags: Google, Amazon, Meta, Bloomberg, Apple, Adobe
Topics: String
String Matching

Approach:
- can just brute force
- but there's also a trick where you can append s to itself to get all rotations
- then use KMP to match pattern to string


Time Complexity: O(n ^ 2)
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for _ in range(len(s)):
            if s == goal:
                return True
            
            s = s[1::] + s[0]
        
        return False



"""
Question:

Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
 

Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:

Input: s = "abcde", goal = "abced"
Output: false
 

Constraints:

1 <= s.length, goal.length <= 100
s and goal consist of lowercase English letters.
"""