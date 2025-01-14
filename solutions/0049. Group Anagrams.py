"""
Title: Group Anagrams
URL: https://leetcode.com/problems/group-anagrams/description/
Difficulty: Medium
Tags: NeetCode 150, Grind, Blind 75, Amazon

Approach:
- could just sort word and use that as key for hashmap
- but counter array gives better time complexity
- declare defaultdict with type list
- iterate through strs and declare count
- iterate through word
-- count[ord(c) - ord('a')] += 1
- d[tuple(count)].append(word)
- return values of dictionary


Time Complexity: O(n * k)
Space Complexity: O(n * k)



Solution:
"""
from template import *

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            d[tuple(count)].append(word)
        
        return d.values()



"""
Question:

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""