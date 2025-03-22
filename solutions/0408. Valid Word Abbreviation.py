"""
Title: Valid Word Abbreviation
URL: https://leetcode.com/problems/valid-word-abbreviation/description/
Difficulty: Easy
Tags: Meta, Datadog, Google, Amazon, Apple, TikTok
Topics: Two Pointers
String

Approach:
- standard two pointer
- but leading zeroes are not allowed so make sure to check if the first number encountered is a 0 or not


Time Complexity: O(m + n)
Space Complexity: O(1)



Solution:
"""
from template import *

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        a = 0
        b = 0

        while a < len(word) and b < len(abbr):
            # get current number
            n = 0
            while b < len(abbr) and abbr[b].isnumeric():
                if n == 0 and int(abbr[b]) == 0:
                    return False
                
                n = n * 10 + int(abbr[b])
                b += 1
            
            # processed a number
            if n > 0:
                a += n
            else:
                if word[a] != abbr[b]:
                    return False
                
                a += 1
                b += 1
        
        return a == len(word) and b == len(abbr)



"""
Question:

A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)
The following are not valid abbreviations:

"s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
"s010n" (has leading zeros)
"s0ubstitution" (replaces an empty substring)
Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.

 

Example 1:

Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").
Example 2:

Input: word = "apple", abbr = "a2e"
Output: false
Explanation: The word "apple" cannot be abbreviated as "a2e".
 

Constraints:

1 <= word.length <= 20
word consists of only lowercase English letters.
1 <= abbr.length <= 10
abbr consists of lowercase English letters and digits.
All the integers in abbr will fit in a 32-bit integer.
"""