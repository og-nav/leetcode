"""
Title: Longest Substring Without Repeating Characters
URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
Difficulty: Medium
Tags: NeetCode 150, Grind, Blind 75, Meta, Google, Amazon, Bloomberg, Popular
Topics: Hash Table
String
Sliding Window

Approach:
- standard sliding window
- use a set to store the state
- there is a one pass solution where you use a hashmap and store the index of the next occurence -> read up on this when preparing for interview
- we add to the window afterwards because set only tells whether the item is in the window or not
-- cause otherwise we would just add and then potentially end up shrinking the entire window incorrectly

Time Complexity: O(n)
Space Complexity: O(1) -> fixed number of english letters, digits, symbols, and spaces



Solution:
"""
from template import *

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        window = set()
        l = 0

        # valid state: all unique characters
        # invalid state: duplicate character
        for r in range(len(s)):
            # invalid state
            while s[r] in window:
                window.remove(s[l])
                l += 1
            
            res = max(res, r - l + 1)
            window.add(s[r])
        
        return res



"""
Question:

Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""