"""
Title: DI String Match
URL: https://leetcode.com/problems/di-string-match/description/
Difficulty: Easy
Tags: Google
Topics: Array
Two Pointers
String
Greedy

Approach:
- can use a stack approach like in 2375 
- or just do 2 pointers and append depending on what the pattern wants



Time Complexity: O(n)
Space Complexity: O(1) or O(n)



Solution:
"""
from template import *

class Solution:
    # 2 pointer
    def diStringMatch(self, s: str) -> List[int]:
        low = 0
        high = len(s)
        res = []
        
        for c in s:
            if c == 'I':
                res.append(low)
                low += 1
            else:
                res.append(high)
                high -= 1
        
        return res + [low]

class Solution:
    # stack
    def diStringMatch(self, s: str) -> List[int]:
        res = []
        stack = []

        for i in range(len(s) + 1):
            stack.append(i)

            if i == len(s) or s[i] == 'I':
                while stack:
                    res.append(stack.pop())
        
        return res



"""
Question:

A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:

s[i] == 'I' if perm[i] < perm[i + 1], and
s[i] == 'D' if perm[i] > perm[i + 1].
Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them.

 

Example 1:

Input: s = "IDID"
Output: [0,4,1,3,2]
Example 2:

Input: s = "III"
Output: [0,1,2,3]
Example 3:

Input: s = "DDI"
Output: [3,2,0,1]
 

Constraints:

1 <= s.length <= 105
s[i] is either 'I' or 'D'.
"""