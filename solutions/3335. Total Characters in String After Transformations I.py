"""
Title: Total Characters in String After Transformations
URL: https://leetcode.com/problems/total-characters-in-string-after-transformations-i/
Difficulty: Medium
Tags: None
Topics: Hash Table
Math
String
Dynamic Programming
Counting

Approach:
- brute force and follow instructions
- need a second counter


Time Complexity: O(m + n) -> m is initial length of string and n is the number of transformations
Space Complexity: O(1) -> only 26 letters



Solution:
"""
from template import *

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        count = defaultdict(int)
        for c in s:
            count[c] += 1
        
        for _ in range(t):
            new_count = defaultdict(int)
            for i in range(1, 26):
                new_count[chr(ord('a') + i)] = count[chr(ord('a') + i - 1)]
            
            new_count['a'] += count['z']
            new_count['b'] += count['z']
            count = new_count
        
        res = 0
        for c in count:
            res += count[c]
            res %= 10 ** 9 + 7
        
        return res



"""
Question:

You are given a string s and an integer t, representing the number of transformations to perform. In one transformation, every character in s is replaced according to the following rules:

If the character is 'z', replace it with the string "ab".
Otherwise, replace it with the next character in the alphabet. For example, 'a' is replaced with 'b', 'b' is replaced with 'c', and so on.
Return the length of the resulting string after exactly t transformations.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: s = "abcyy", t = 2

Output: 7

Explanation:

First Transformation (t = 1):
'a' becomes 'b'
'b' becomes 'c'
'c' becomes 'd'
'y' becomes 'z'
'y' becomes 'z'
String after the first transformation: "bcdzz"
Second Transformation (t = 2):
'b' becomes 'c'
'c' becomes 'd'
'd' becomes 'e'
'z' becomes "ab"
'z' becomes "ab"
String after the second transformation: "cdeabab"
Final Length of the string: The string is "cdeabab", which has 7 characters.
Example 2:

Input: s = "azbk", t = 1

Output: 5

Explanation:

First Transformation (t = 1):
'a' becomes 'b'
'z' becomes "ab"
'b' becomes 'c'
'k' becomes 'l'
String after the first transformation: "babcl"
Final Length of the string: The string is "babcl", which has 5 characters.
 

Constraints:

1 <= s.length <= 105
s consists only of lowercase English letters.
1 <= t <= 105
"""