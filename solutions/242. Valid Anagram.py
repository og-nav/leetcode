"""
Title: Valid Anagram
URL: https://leetcode.com/problems/valid-anagram/description/
Difficulty: Easy
Tags: NeetCode 150, Grind, Blind 75

Approach:
- one liner can just use frequency hashmap for both strings
- otherwise, we want to populate one hashmap with characters and count for one string
- next, we want to iterate through t and decrement
-- can return false if current count is 0 or character isn't in the hashmap
- lastly, we want to make sure all values in hashmap are 0

- follow up, what if inputs contain unicode characters? how would that change answer?
-- answer, we stick to hashmap since there are over 1 million unicode characters so array might get very large.
-- using hashmap allows memory/space to be allocated as needed instead of upfront.


Time Complexity: O(s + t) -> since we iterate through both strings once
Space Complexity: O(1) -> per problem constraints, we only store a-z. if it was unicode or something else, it would 
                          be O(n)



Solution:
"""
from template import *

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s) == Counter(t)
        d = defaultdict(int)
        for c in s:
            d[c] += 1
        
        for c in t:
            if c not in d or d[c] == 0:
                return False
            d[c] -= 1
        
        return not any(d.values())



"""
Question:

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""