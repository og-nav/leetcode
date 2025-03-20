"""
Title: Unique Length-3 Palindromic Subsequences
URL: https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description/
Difficulty: Medium
Tags: Google, Meta, Amazon, Bloomberg, Adobe, Apple, Uber
Topics: Hash Table
String
Bit Manipulation
Prefix Sum

Approach:
- iterate through s and find left and right indices of each letter in alphabet
- then iterate through each letter in the alphabet and for each letter, iterate from it's left index + 1 to its right index + 1 and add the palindromic subsequence to a set
- return the length of the set


Time Complexity: O(n) -> technically, but if more letters were used beyond the 26, it would be O(n ^ 2)
Space Complexity: O(n) -> same



Solution:
"""
from template import *

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left_index = [-1] * 26
        right_index = [-1] * 26

        for i, c in enumerate(s):
            letter = ord(c) - ord('a')
            if left_index[letter] == -1:
                left_index[letter] = i
            else:
                right_index[letter] = i
        
        res = set()
        for i in range(26):
            if left_index[i] != -1 and right_index[i] != -1:
                for m in range(left_index[i] + 1, right_index[i]):
                    res.add(chr(ord('a') + i) + s[m] + chr(ord('a') + i))

        return len(res)



"""
Question:

Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
 

Example 1:

Input: s = "aabca"
Output: 3
Explanation: The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "aabca")
- "aaa" (subsequence of "aabca")
- "aca" (subsequence of "aabca")
Example 2:

Input: s = "adc"
Output: 0
Explanation: There are no palindromic subsequences of length 3 in "adc".
Example 3:

Input: s = "bbcbaba"
Output: 4
Explanation: The 4 palindromic subsequences of length 3 are:
- "bbb" (subsequence of "bbcbaba")
- "bcb" (subsequence of "bbcbaba")
- "bab" (subsequence of "bbcbaba")
- "aba" (subsequence of "bbcbaba")
 

Constraints:

3 <= s.length <= 105
s consists of only lowercase English letters.
"""