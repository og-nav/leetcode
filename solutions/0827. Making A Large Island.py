"""
Title: Making A Large Island
URL: https://leetcode.com/problems/making-a-large-island/description/
Difficulty: Hard
Tags: Meta, AirBnB, Amazon, Google, Microsoft, TikTok, DoorDash, Uber
Topics: Array
Depth-First Search
Breadth-First Search
Union Find
Matrix

Approach:
- brute force of flipping a 0 to a 1 and finding island size gives TLE
- we want to explore all islands and number each island
- then save each number's size
- then at the end, we only need to check 4 directionally to see if we bridge new islands
-- use a set to avoid double counting the same island
-- also we can really only connect at most 4 unique islands to each other
- and then just add up the sizes of islands that are now touching
- I read a comment calling this "island coloring" and it made a lot of sense to me.


Time Complexity: O(m * n)
Space Complexity: O(m * n)



Solution:
"""
from template import *

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def invalid(r, c):
            return r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0])
        
        island_squares = defaultdict(int) # coordinate -> island number that it belongs to
        island_sizes = defaultdict(int) # island number -> its size
        island = 0 # size of current island we are exploring
        island_number = 0 # starting island number

        def dfs(r, c, current_island_number):
            nonlocal island
            if invalid(r, c) or grid[r][c] == 0 or (r, c) in island_squares:
                return
            
            island_squares[(r, c)] = current_island_number
            island += 1
            for dr, dc in directions:
                dfs(r + dr, c + dc, current_island_number)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in island_squares:
                    # explore this island
                    dfs(i, j, island_number)
                    island_sizes[island_number] = island
                    island = 0
                    island_number += 1
        
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    islands_to_add = set() # islands we need to add to the total
                    tentative_island_size = 1
                    for dr, dc in directions:
                        if not invalid(r + dr, c + dc) and (r + dr, c + dc) in island_squares:
                            islands_to_add.add(island_squares[(r + dr, c + dc)])
                    
                    # now add up islands
                    for island_number in islands_to_add:
                        tentative_island_size += island_sizes[island_number]
                    
                    res = max(res, tentative_island_size)
        
        if res == 0: # water not found
            return len(grid) * len(grid[0])
        
        return res



"""
Question:

You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

 

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 500
grid[i][j] is either 0 or 1.
"""