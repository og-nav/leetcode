"""
Title: Valid Parentheses
URL: https://leetcode.com/problems/valid-parentheses/description/
Difficulty: Easy
Tags: NeetCode 150, Grind, Blind 75, Amazon, Meta, Microsoft

Approach:
- basically want to use a stack and iterate through s
- any time we encounter a closing element, we want to check if the stack has values and if the popped value is the matching opening
- if not, we can return False
- lastly, stack may not be empty in the end. for example s = "(((". we need to make sure stack is empty, so return not stack


Time Complexity: O(n)
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = '({['
        for c in s:
            if c in opening:
                stack.append(c)
            elif c == ')':
                if not stack or stack.pop() != '(':
                    return False
            elif c == '}':
                if not stack or stack.pop() != '{':
                    return False
            elif c == ']':
                if not stack or stack.pop() != '[':
                    return False
        
        return not stack



"""
Question:

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'
"""