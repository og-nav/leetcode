"""
Title: Find All Anagrams in a String
URL: https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
Difficulty: Medium
Tags: Grind, Meta, Snowflake, Amazon, Google, Microsoft, Bloomberg, Apple, TikTok, Databricks
Topics: String, Sliding Window, Hash Table

Approach:
- standard sliding window where the window is a hashmap of the count of the current window
- shrink the window when the current character is too large in p count hashmap
-- make sure to delete the character from the window if the count reaches 0
- lastly, check if the window is an anagram of p by comparing the hashmaps
-- make sure to check in both directions -> iterate through s_count and p_count


Time Complexity: O(n)
Space Complexity: O(1) -> only 26 characters in the hashmap



Solution:
"""
from template import *

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def is_anagram(s_count, p_count):
            for c in s_count:
                if s_count[c] != p_count[c]:
                    return False
            
            for c in p_count:
                if p_count[c] != s_count[c]:
                    return False
            
            return True
        
        count = defaultdict(int)
        for c in p:
            count[c] += 1
        
        window = defaultdict(int)
        res = []
        l = 0
        for r in range(len(s)):
            window[s[r]] += 1
            while window[s[r]] > count[s[r]]:
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1
            
            if is_anagram(window, count):
                res.append(l)
        
        return res



"""
Question:

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
"""