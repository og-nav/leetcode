"""
Title: Palindrome Permutation
URL: https://leetcode.com/problems/palindrome-permutation/description/
Difficulty: Easy
Tags: Meta, Microsoft, Google, Bloomberg
Topics: Hash Table
String
Bit Manipulation

Approach:
- need to realize a palindrome can only have 1 frequency of odd characters
- therefore, we can add characters to a set and remove them if we encounter a duplicate
- therefore, only characters with an odd count will be left in the set at the end
- therefore, we only need to make sure the length of the set is less than 2


Time Complexity: O(n)
Space Complexity: O(1)



Solution:
"""
from template import *

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        characters = set()
        for c in s:
            if c in characters:
                characters.remove(c)
            else:
                characters.add(c)
        
        return len(characters) <= 1



"""
Question:

Given a string s, return true if a permutation of the string could form a palindrome and false otherwise.

 

Example 1:

Input: s = "code"
Output: false
Example 2:

Input: s = "aab"
Output: true
Example 3:

Input: s = "carerac"
Output: true
 

Constraints:

1 <= s.length <= 5000
s consists of only lowercase English letters.
"""