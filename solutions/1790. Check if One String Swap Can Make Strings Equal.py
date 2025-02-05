"""
Title: Check if One String Swap Can Make Strings Equal
URL: https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/
Difficulty: Easy
Tags: DoorDash, Meta, Amazon
Topics: Hash Table
String
Counting

Approach:
- make sure strings have the same letters
- and count differences
- return if difference is less than 3


Time Complexity: O(n)
Space Complexity: O(1) -> counter will only hold 26 characters at most



Solution:
"""
from template import *

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if Counter(s1) != Counter(s2):
            return False
        
        difference = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                difference += 1
        
        return difference < 3



"""
Question:

You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

 

Example 1:

Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".
Example 2:

Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.
Example 3:

Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.
 

Constraints:

1 <= s1.length, s2.length <= 100
s1.length == s2.length
s1 and s2 consist of only lowercase English letters.
"""