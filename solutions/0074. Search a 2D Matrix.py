"""
Title: Search a 2D Matrix
URL: https://leetcode.com/problems/search-a-2d-matrix/description/
Difficulty: Medium
Tags: NeetCode 150, Grind, Amazon, Bloomberg, Meta, Google, Microsoft, Adobe, Apple
Topics: Array
Binary Search
Matrix

Approach:
- binary search on first elements to find the correct row
- then binary search on the row to find the number if it exists
- note for vertical binary search
-- we need to use b and NOT t in the second horizontal search
-- this because we adjust b if the row is too big
--- we subtract 1, which might make it less than t which is what is needed if they were both equal originally
-- we want to err on the smaller side, which means if t is incremented and then the loop breaks, we want the smaller number


Time Complexity: O(log(m * n)) -> log(m) + log(n)
Space Complexity: O(1)



Solution:
"""
from template import *

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix) - 1
        l, r = 0, len(matrix[0]) - 1

        while t <= b:
            m = (t + b) // 2
            if matrix[m][0] == target:
                return True
            elif matrix[m][0] > target:
                b = m - 1
            else:
                t = m + 1
        
        while l <= r:
            m = (l + r) // 2
            if matrix[b][m] == target:
                return True
            elif matrix[b][m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return False



"""
Question:

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""