"""
Title: Pascal's Triangle
URL: https://leetcode.com/problems/pascals-triangle/description/
Difficulty: Easy
Tags: Google, Meta, Amazon, Bloomberg, Microsoft, Adobe, Uber, Yahoo
Topics: Array
Dynamic Programming

Approach:
- very edge case heavy
- need to remember to start for loops at 1 
- main difficulty is setting up the result 2d array


Time Complexity: O(n^2)
Space Complexity: O(1) -> result does not count towards space complexity



Solution:
"""
from template import *

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1 for _ in range(1, i + 1)] for i in range(1, numRows + 1)]
        for i in range(1, numRows):
            for j in range(1, i):
                res[i][j] = res[i - 1][j] + res[i - 1][j - 1]
        
        return res



"""
Question:

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
"""