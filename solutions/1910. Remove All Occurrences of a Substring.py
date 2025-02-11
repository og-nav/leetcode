"""
Title: Remove All Occurrences of a Substring
URL: https://leetcode.com/problems/remove-all-occurrences-of-a-substring/description/
Difficulty: Medium
Tags: Microsoft, Google, Amazon, Bloomberg
Topics: String
Stack
Simulation

Approach:
- iterate through s while appending to a stack
- if stack suffix is equal to part, we just pop the stack
- finally, we need to run one last pop in the end in case the last add inadvertently created a part suffix


Time Complexity: O(m * n) -> iterate thru s while checking len(part) per iteration
Space Complexity: O(m + n) -> for stack and part



Solution:
"""
from template import *

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part = [c for c in part]
        for c in s:
            if len(stack) >= len(part) and stack[len(stack) - len(part): len(stack)] == part:
                for _ in range(len(part)):
                    stack.pop()
            stack.append(c)
        
        # last pop
        if len(stack) >= len(part) and stack[len(stack) - len(part): len(stack)] == part:
                for _ in range(len(part)):
                    stack.pop()
        
        return "".join(stack)



"""
Question:

Given two strings s and part, perform the following operation on s until all occurrences of the substring part are removed:

Find the leftmost occurrence of the substring part and remove it from s.
Return s after removing all occurrences of part.

A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: s = "daabcbaabcbc", part = "abc"
Output: "dab"
Explanation: The following operations are done:
- s = "daabcbaabcbc", remove "abc" starting at index 2, so s = "dabaabcbc".
- s = "dabaabcbc", remove "abc" starting at index 4, so s = "dababc".
- s = "dababc", remove "abc" starting at index 3, so s = "dab".
Now s has no occurrences of "abc".
Example 2:

Input: s = "axxxxyyyyb", part = "xy"
Output: "ab"
Explanation: The following operations are done:
- s = "axxxxyyyyb", remove "xy" starting at index 4 so s = "axxxyyyb".
- s = "axxxyyyb", remove "xy" starting at index 3 so s = "axxyyb".
- s = "axxyyb", remove "xy" starting at index 2 so s = "axyb".
- s = "axyb", remove "xy" starting at index 1 so s = "ab".
Now s has no occurrences of "xy".
 

Constraints:

1 <= s.length <= 1000
1 <= part.length <= 1000
s​​​​​​ and part consists of lowercase English letters.
"""