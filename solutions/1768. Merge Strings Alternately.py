"""
Title: Merge Strings Alternately
URL: https://leetcode.com/problems/merge-strings-alternately/description/
Difficulty: Easy
Tags: Google, Microsoft, Meta, Amazon, Bloomberg, Apple, Adobe, Popular
Topics: Two Pointers
String

Approach:
- two pointers or single pointer


Time Complexity: O(m + n)
Space Complexity: O(m + n) -> can be reduced to O(1) if not using Pythonic style at the end when returning



Solution:
"""
from template import *

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a, b = 0, 0
        res = []

        while a < len(word1) and b < len(word2):
            res.append(word1[a])
            res.append(word2[b])

            a += 1
            b += 1
        
        if a < len(word1):
            return "".join(res) + word1[a::]
        elif b < len(word2):
            return "".join(res) + word2[b::]
        else:
            return "".join(res)



"""
Question:

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 

Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
"""