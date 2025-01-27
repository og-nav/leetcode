"""
Title: Is Subsequence
URL: https://leetcode.com/problems/is-subsequence/description/
Difficulty: Easy
Tags: Meta, Amazon, Google, Microsoft, Pinterest, Uber, Adobe, Apple
Topics: Two Pointers
String
Dynamic Programming

Approach:
- two pointer
- if s[i] == t[j], increment i
- always increment j
- return if i == len(s) at the end
- to answer the follow up, we want to create a hashmap where each character in t is associated with an array
-- with all of its positions in the string. then, we can perform binary search (or linear) to find the index. we need 
-- one last step where we make sure the index moves monotonically upwards.


Time Complexity: O(t) 
Space Complexity: O(1)



Solution:
"""
from template import *

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return i == len(s)



"""
Question:

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
"""