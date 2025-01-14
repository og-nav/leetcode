"""
Title: Rotting Oranges
URL: https://leetcode.com/problems/rotting-oranges/description/
Difficulty: Medium
Tags: NeetCode 150, Grind, Amazon

Approach:
- standard multi-source BFS with caveats
- want to iterate once through grid and count number of fresh oranges and save coordinates of rotten oranges
- IMPORTANT: if fresh == 0 -> we return 0. once this is done, we can do basic BFS where we make sure we haven't
-- WATCH OUT FOR THIS EDGE CASE: [[0]] -> return 0
-- visted neighbors before appending to queue
- keep time variable as -1, increment it each discrete BFS layer
- if we encounter fresh orange, decrement fresh by 1
- if fresh is ever 0, we know we have turned all oranges rotten; return time
- lastly, make sure every 4-directionally adjacent square added to the queue is a fresh orange.
-- if invalid r + dr, c + dc, () in visit or grid[][] != 1, continue
- return -1 if we finish BFS cuz there are still fresh oranges available


Time Complexity: O(m * n) -> we visit each square twice (once for populating, once for BFS)
Space Complexity: O(m * n) -> visit set holds all squares



Solution:
"""
from template import *

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def invalid(r, c):
            return r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0])
        
        fresh = 0
        rotten = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotten.append((i, j))
        
        if fresh == 0:
            return 0
        
        queue = deque(rotten)
        visit = set(rotten)
        time = -1
        while queue:
            time += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()

                if grid[r][c] == 1:
                    fresh -= 1
                if fresh == 0:
                    return time

                for dr, dc in directions:
                    if invalid(r + dr, c + dc) or (r + dr, c + dc) in visit or grid[r + dr][c + dc] != 1:
                        continue
                    
                    queue.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))
        
        return -1



"""
Question:

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""