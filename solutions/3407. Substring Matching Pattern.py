"""
Title: Substring Matching Problem
URL: https://leetcode.com/problems/substring-matching-pattern/description/
Difficulty: Easy
Tags: Amazon
Topics: String
String Matching

Approach:
- very tricky problem with a lot of edge cases despite being an "easy"
- need to realize that you need to split up the pattern by the "*"
- then search the string for the prefix
- if not found, return false
- if found, then start searching from the next index to the end for the suffix
- if found, return true, else return false
- could use KMP or Rabin Karp to further reduce time complexity to O(m + n)


Time Complexity: O(m * n)
Space Complexity: O(n) -> pattern gets split into an array



Solution:
"""
from template import *

class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        p = p.split('*')
        prefix = p[0]
        suffix = p[1]
        prefix_end = 0

        for i in range(len(prefix), len(s) + 1):
            if s[i - len(prefix): i] == prefix:
                prefix_end = i
                break
        else:
            return False
        
        for i in range(prefix_end + len(suffix), len(s) + 1):
            if s[i - len(suffix): i] == suffix:
                return True

        return False



"""
Question:

You are given a string s and a pattern string p, where p contains exactly one '*' character.

The '*' in p can be replaced with any sequence of zero or more characters.

Return true if p can be made a 
substring
 of s, and false otherwise.

 

Example 1:

Input: s = "leetcode", p = "ee*e"

Output: true

Explanation:

By replacing the '*' with "tcod", the substring "eetcode" matches the pattern.

Example 2:

Input: s = "car", p = "c*v"

Output: false

Explanation:

There is no substring matching the pattern.

Example 3:

Input: s = "luck", p = "u*"

Output: true

Explanation:

The substrings "u", "uc", and "uck" match the pattern.

 

Constraints:

1 <= s.length <= 50
1 <= p.length <= 50 
s contains only lowercase English letters.
p contains only lowercase English letters and exactly one '*'
"""