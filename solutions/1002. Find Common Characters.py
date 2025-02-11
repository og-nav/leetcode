"""
Title: Find Common Characters
URL: https://leetcode.com/problems/find-common-characters/description/
Difficulty: Easy
Tags: Google, Amazon, Bloomberg, Meta, Microsoft, Apple
Topics: Array
Hash Table
String

Approach:
- create a counter for the first word
- then iterate through words while creating a counter for each word
- then iterate through the starting counter and set it's value to the min of 
-- the current value or the current word's value


Time Complexity: O(m * n) -> len of the words array * each word
Space Complexity: O(1) -> Counter only uses up to 26 characters



Solution:
"""
from template import *

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        start = defaultdict(int)
        for c in words[0]:
            start[c] += 1
        
        for i in range(1, len(words)):
            curr = defaultdict(int)
            for c in words[i]:
                curr[c] += 1
            
            for c in start:
                start[c] = min(start[c], curr[c])
        
        res = []
        for c in start:
            for _ in range(start[c]):
                res.append(c)
        
        return res



"""
Question:

Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
"""