"""
Title: Maximum Number of Fish in a Grid
URL: https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/description/
Difficulty: Medium
Tags: None
Topics: Array
Depth-First Search
Breadth-First Search
Union Find
Matrix

Approach:
- very similar to number of islands and max area of island
- just need an integer for number of fish, then after each dfs, res = max(res, fish)
- make sure to reset fish after each dfs


Time Complexity: O(m * n)
Space Complexity: O(m * n)



Solution:
"""
from template import *

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        res = 0
        fish = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit = set()
        def invalid(r, c):
            return r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0])
        
        def dfs(r, c):
            nonlocal fish
            if invalid(r, c) or (r, c) in visit or grid[r][c] == 0:
                return
            
            visit.add((r, c))
            fish += grid[r][c]
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0 and (i, j) not in visit:
                    dfs(i, j)
                    res = max(res, fish)
                    fish = 0
        
        return res



"""
Question:

You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:

A land cell if grid[r][c] = 0, or
A water cell containing grid[r][c] fish, if grid[r][c] > 0.
A fisher can start at any water cell (r, c) and can do the following operations any number of times:

Catch all the fish at cell (r, c), or
Move to any adjacent water cell.
Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.

An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.

 

Example 1:


Input: grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
Output: 7
Explanation: The fisher can start at cell (1,3) and collect 3 fish, then move to cell (2,3) and collect 4 fish.
Example 2:


Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
Output: 1
Explanation: The fisher can start at cells (0,0) or (3,3) and collect a single fish. 
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
0 <= grid[i][j] <= 10
"""