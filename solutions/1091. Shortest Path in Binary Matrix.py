"""
Title: Shortest Path in Binary Matrix
URL: https://leetcode.com/problems/shortest-path-in-binary-matrix/description/
Difficulty: Medium
Tags: Meta

Approach:
- pretty much BFS
- quick base case check if grid[0][0] or grid[-1][-1] == 1, and return -1 if so since it would be impossible to finish
- in BFS, follow node-based bfs where you make sure neighbor node (r + dr, c + dc) is valid to add to queue, 
-- add to queue, then add to visit
-- important to add to visit here and not do dfs style because you might repeatedly add visited nodes to visit
- Mention A* algorithm, but idk how to implement


Time Complexity: O(m * n) -> or O(n ^ 2) since it is n * n
Space Complexity: O(m * n) -> cuz visit set holds all squares



Solution:
"""
from template import *

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]
        def invalid(r, c):
            return r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0])
        
        visit = set([(0, 0)])
        queue = deque([(0, 0)])
        distance = 0
        while queue:
            distance += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == len(grid) - 1 and c == len(grid) - 1:
                    return distance

                for dr, dc in directions:
                    if invalid(r + dr, c + dc) or (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1:
                        continue
                    
                    queue.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))
        
        return -1



"""
Question:

Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

 

Example 1:


Input: grid = [[0,1],[1,0]]
Output: 2
Example 2:


Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
"""