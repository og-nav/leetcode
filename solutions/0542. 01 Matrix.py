"""
Title: 01 Matrix
URL: https://leetcode.com/problems/01-matrix/description/
Difficulty: Medium
Tags: Grind, Amazon, Google, Meta, Microsoft, Adobe, Apple, Bloomberg, TikTok, Snowflake
Topics: Array
Dynamic Programming
Breadth-First Search
Matrix

Approach:
- basically need to do multi-source bfs starting from 0s instead of 1s
- first time encountering a 1 automatically means it's the shortest path


Time Complexity: O(m * n)
Space Complexity: O(m * n)



Solution:
"""
from template import *

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        res = [[-1 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def invalid(r, c):
            return r < 0 or c < 0 or r >= len(mat) or c >= len(mat[0])

        queue = deque([])
        visit = set()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i, j, 0)) # (r, c, distance)
                    visit.add((i, j))
                    res[i][j] = 0
        
        while queue:
            for _ in range(len(queue)):
                r, c, distance = queue.popleft()
                if res[r][c] == -1: 
                    res[r][c] = distance
                
                for dr, dc in directions:
                    if not invalid(r + dr, c + dc) and (r + dr, c + dc) not in visit:
                        queue.append((r + dr, c + dc, distance + 1))
                        visit.add((r + dr, c + dc))
        
        return res                               



"""
Question:

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two cells sharing a common edge is 1.

 

Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
"""