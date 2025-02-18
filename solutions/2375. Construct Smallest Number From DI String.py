"""
Title: Construct Smallest Number From DI String
URL: https://leetcode.com/problems/construct-smallest-number-from-di-string/description/
Difficulty: Medium
Tags: Goldman Sachs, Amazon
Topics: String
Backtracking
Stack
Greedy

Approach:
- most intuitive is to use backtracking and generate all valid combinations 
-- need an index that iterates through pattern as well as an available numbers set
- then only append higher or lower numbers than the last number depending on the pattern

- can also do in O(n) time using a stack by being greedy
-- we start from 0 and fill up the stack
-- once we encounter an I, we clear the stack into the result
-- note that emptying the stack into res flips the order to decreasing


Time Complexity: O(n! * n ^ 2) or O(n)
Space Complexity: O(n) for both



Solution:
"""
from template import *

class Solution:
    # stack
    def smallestNumber(self, pattern: str) -> str:
        res = []
        stack = []

        for i in range(len(pattern) + 1):
            stack.append(str(i + 1))

            if i == len(pattern) or pattern[i] == "I":
                while stack:
                    res.append(stack.pop())
            
        return "".join(res)

class Solution:
    # backtracking
    def smallestNumber(self, pattern: str) -> str:
        possible = []

        def backtrack(i, curr, available):
            if i == len(pattern):
                possible.append(curr)
                return

            prev = int(curr[-1])
            if pattern[i] == "I":
                for j in range(prev, 10):
                    if j in available:
                        available.remove(j)
                        backtrack(i + 1, curr + str(j), available)
                        available.add(j)
            else:
                for j in range(1, prev):
                    if j in available:
                        available.remove(j)
                        backtrack(i + 1, curr + str(j), available)
                        available.add(j)

        for i in range(1, 10):
            before = [x for x in range(1, i)]
            after = [x for x in range(i + 1, 10)]
            backtrack(0, str(i), set(before + after))
        
        possible.sort()
        return possible[0]



"""
Question:

You are given a 0-indexed string pattern of length n consisting of the characters 'I' meaning increasing and 'D' meaning decreasing.

A 0-indexed string num of length n + 1 is created using the following conditions:

num consists of the digits '1' to '9', where each digit is used at most once.
If pattern[i] == 'I', then num[i] < num[i + 1].
If pattern[i] == 'D', then num[i] > num[i + 1].
Return the lexicographically smallest possible string num that meets the conditions.

 

Example 1:

Input: pattern = "IIIDIDDD"
Output: "123549876"
Explanation:
At indices 0, 1, 2, and 4 we must have that num[i] < num[i+1].
At indices 3, 5, 6, and 7 we must have that num[i] > num[i+1].
Some possible values of num are "245639871", "135749862", and "123849765".
It can be proven that "123549876" is the smallest possible num that meets the conditions.
Note that "123414321" is not possible because the digit '1' is used more than once.
Example 2:

Input: pattern = "DDD"
Output: "4321"
Explanation:
Some possible values of num are "9876", "7321", and "8742".
It can be proven that "4321" is the smallest possible num that meets the conditions.
 

Constraints:

1 <= pattern.length <= 8
pattern consists of only the letters 'I' and 'D'.
"""