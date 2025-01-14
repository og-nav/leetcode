"""
Title: Valid Palindrome II
URL: https://leetcode.com/problems/valid-palindrome-ii/description/
Difficulty: Easy
Tags: Meta

Approach:
- want to do two pointers starting from each end
- if we ever encounter a place where s[l] != s[r], we want to check if the middle of the string is a palindrome
- needs to be checked twice, once where you ignore s[l] and once where you ignore s[r]
- if it is a palindrome after skipping, return True, else return False
- return True at the end because the original string is a palindrome and question asks for "at most one"


Time Complexity: O(n)
Space Complexity: O(n) -> NOTE: this approach might use extra space because of substring using the indexes
                                - we could just have a separate function that checks for palindrome using same
                                - two pointer method. this would be O(1) space



Solution:
"""
from template import *

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                if s[l + 1: r + 1] == s[l + 1: r + 1][::-1] or s[l: r] == s[l: r][::-1]:
                    return True
                return False

            l += 1
            r -= 1
        
        return True



"""
Question:

Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
"""