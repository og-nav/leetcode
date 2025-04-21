"""
Title: Permutation in String
URL: https://leetcode.com/problems/permutation-in-string/description/
Difficulty: Medium
Tags: NeetCode 150, Google, Amazon, Meta, Microsoft, Cisco, Bloomberg, Apple, TikTok
Topics: Hash Table
Two Pointers
String
Sliding Window

Approach:
- contains a permutation just means that the window's character count is the same as s1's character count
- then to shrink the window, the while condition is while the window's character count of the added letter is 
-- greater than its respective count in s1
--- defaultdict returns 0 if it doesn't exist so any extraneous letters will automatically be removed


Time Complexity: O(m + n)
Space Complexity: O(1) # only O(26)



Solution:
"""
from template import *

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = defaultdict(int)
        for c in s1:
            count[c] += 1
        
        window = defaultdict(int)
        l = 0
        for r in range(len(s2)):
            # add element to window
            window[s2[r]] += 1

            # shrink window if invalid
            while window[s2[r]] > count[s2[r]]:
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    del window[s2[l]]
                l += 1
            
            # now that window is "valid," check for match (O(1) since only 26 letters and numbers)
            if window == count:
                return True
        
        return False



"""
Question:

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""