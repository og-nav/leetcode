'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''
from collections import deque
from typing import List


class Solution:
    def numIslandsDFS(self, grid: List[List[str]]) -> int:
        res = 0
        visit = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        def invalid(r, c):
            return r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0])
        
        def dfs(r, c):
            if invalid(r, c) or (r, c) in visit or grid[r][c] == "0":
                return
            
            visit.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visit:
                    res += 1
                    dfs(i, j)
        
        return res
    

    def numIslandsBFS(self, grid: List[List[str]]) -> int:
        res = 0
        visit = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        def invalid(r, c):
            return r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0])
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visit:
                    res += 1
                    queue = deque([(i, j)])
                    while queue:
                        for _ in range(len(queue)):
                            r, c = queue.popleft()
                            if invalid(r, c) or (r, c) in visit or grid[r][c] == "0":
                                continue
                            
                            visit.add((r, c))
                            for dr, dc in directions:
                                queue.append((r + dr, c + dc))
        
        return res
