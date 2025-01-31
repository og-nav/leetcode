"""
Title: Custom Sort String
URL: https://leetcode.com/problems/custom-sort-string/description/
Difficulty: Medium
Tags: Meta, Amazon, Microsoft, Uber, Bloomberg, Adobe, Snap
Topics: String, Stack, etc

Approach:
- exact same solution as 1122. Relative Sort Array just with strings
- also need to make sure to not make the same mistake of not iterating for _ in range(counts[key]) at the end
-- when adding on the extra letters


Time Complexity: O(n) -> n for s and the 1 for order cuz order only has one of each letter so max 26
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1
        
        res = ""
        for c in order:
            for _ in range(counts[c]):
                res += c
            del counts[c]
        
        for key in counts:
            for _ in range(counts[key]):
                res += key
        
        return res



"""
Question:

You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.

Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

Return any permutation of s that satisfies this property.

 

Example 1:

Input: order = "cba", s = "abcd"

Output: "cbad"

Explanation: "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a".

Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.

Example 2:

Input: order = "bcafg", s = "abcd"

Output: "bcad"

Explanation: The characters "b", "c", and "a" from order dictate the order for the characters in s. The character "d" in s does not appear in order, so its position is flexible.

Following the order of appearance in order, "b", "c", and "a" from s should be arranged as "b", "c", "a". "d" can be placed at any position since it's not in order. The output "bcad" correctly follows this rule. Other arrangements like "dbca" or "bcda" would also be valid, as long as "b", "c", "a" maintain their order.

 

Constraints:

1 <= order.length <= 26
1 <= s.length <= 200
order and s consist of lowercase English letters.
All the characters of order are unique.
"""