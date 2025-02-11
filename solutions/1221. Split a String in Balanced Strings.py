"""
Title: Split a String in Balanced Strings
URL: https://leetcode.com/problems/split-a-string-in-balanced-strings/description/
Difficulty: Easy
Tags: Amazon
Topics: String
Greedy
Counting

Approach:
- need to read the question
- and realize that every time you split the string, we must consider both substrings
- we can do it greedy with a diff
- for some reason, I had thought that we need to count up all substrings rather than just partition the string


Time Complexity: O(n)
Space Complexity: O(1)



Solution:
"""
from template import *

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        diff = 0
        res = 0
        for i in range(len(s)):
            if s[i] == 'R':
                diff += 1
            else:
                diff -= 1
            
            if diff == 0:
                res += 1
        
        return res



"""
Question:

Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it into some number of substrings such that:

Each substring is balanced.
Return the maximum number of balanced strings you can obtain.

 

Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
Example 2:

Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", each substring contains same number of 'L' and 'R'.
Note that s cannot be split into "RL", "RR", "RL", "LR", "LL", because the 2nd and 5th substrings are not balanced.
Example 3:

Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".
 

Constraints:

2 <= s.length <= 1000
s[i] is either 'L' or 'R'.
s is a balanced string.
"""