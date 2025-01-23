"""
Title: First Completely Painted Row or Column
URL: https://leetcode.com/problems/first-completely-painted-row-or-column/description/
Difficulty: Medium
Tags: Citadel, Adobe
Topics: Array
Hash Table
Matrix

Approach:
- idea is to have a row map and col map to store the row and col of each element (since all elements are unique)
-- ex: a number 9 at row 0 and col 1 would be stored as row_map[9] = 0 and col_map[9] = 1
- then we need a rows array and cols array that store the frequency of how many times a particular
-- row or column has been hit
- doing this is very tedious
- trick to watch out for:
  - a row adds up to the length of mat[0]
  - and a col adds up to the length of mat


Time Complexity: O(m * n)
Space Complexity: O(m * n)



Solution:
"""
from template import *

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows = [0 for _ in range(len(mat))]
        cols = [0 for _ in range(len(mat[0]))]
        row_map = defaultdict(int)
        col_map = defaultdict(int)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                row_map[mat[i][j]] = i
                col_map[mat[i][j]] = j
        
        for i in range(len(arr)):
            rows[row_map[arr[i]]] += 1
            cols[col_map[arr[i]]] += 1
            
            if rows[row_map[arr[i]]] == len(mat[0]) or cols[col_map[arr[i]]] == len(mat):
                return i
        
        return 0



"""
Question:

You are given a 0-indexed integer array arr, and an m x n integer matrix mat. arr and mat both contain all the integers in the range [1, m * n].

Go through each index i in arr starting from index 0 and paint the cell in mat containing the integer arr[i].

Return the smallest index i at which either a row or a column will be completely painted in mat.

 

Example 1:

image explanation for example 1
Input: arr = [1,3,4,2], mat = [[1,4],[2,3]]
Output: 2
Explanation: The moves are shown in order, and both the first row and second column of the matrix become fully painted at arr[2].
Example 2:

image explanation for example 2
Input: arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]]
Output: 3
Explanation: The second column becomes fully painted at arr[3].
 

Constraints:

m == mat.length
n = mat[i].length
arr.length == m * n
1 <= m, n <= 105
1 <= m * n <= 105
1 <= arr[i], mat[r][c] <= m * n
All the integers of arr are unique.
All the integers of mat are unique.
"""