"""
Title: Find K-Length Substrings With No Repeated Characters
URL: https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/description/
Difficulty: Medium
Tags: Amazon
Topics: Hash Table
String
Sliding Window

Approach:
- dynamic window sliding window
- also increment l when we increment the result because we want only a max window size of k


Time Complexity: O(n)
Space Complexity: O(1) -> set can only contain 26 letters



Solution:
"""
from template import *

class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if k > len(s):
            return 0
        
        window = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            
            window.add(s[r])
            if r - l + 1 == k:
                res += 1
                window.remove(s[l])
                l += 1
        
        return res



"""
Question:

Given a string s and an integer k, return the number of substrings in s of length k with no repeated characters.

 

Example 1:

Input: s = "havefunonleetcode", k = 5
Output: 6
Explanation: There are 6 substrings they are: 'havef','avefu','vefun','efuno','etcod','tcode'.
Example 2:

Input: s = "home", k = 5
Output: 0
Explanation: Notice k can be larger than the length of s. In this case, it is not possible to find any substring.
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
1 <= k <= 104
"""