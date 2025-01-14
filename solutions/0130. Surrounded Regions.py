"""
Title: Surrounded Regions
URL: https://leetcode.com/problems/surrounded-regions/description/
Difficulty: Medium
Tags: NeetCode 150

Approach:
- not so straightforward -> I get this wrong quite often. practice once before looking at solution
- basically, want to do number of islands but with an out_of_bounds flag and a set that holds the island
- important: isntead of waiting till end to update all squares, can just update them as they come as long as
-- out_of_bounds is false
- there is a weird quirk where if I check for if out_of_bounds or invalid(r, c), the code fails.
                                              needs to just be if invalid(r, c)


Time Complexity: O(m * n)
Space Complexity: O(m * n)



Solution:
"""
from template import *

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def invalid(r, c):
            return r < 0 or c < 0 or r >= len(board) or c >= len(board[0])
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit = set()
        region = set()
        out_of_bounds = False

        def dfs(r, c):
            nonlocal out_of_bounds
            if invalid(r, c):
                out_of_bounds = True
                return

            if (r, c) in visit or board[r][c] == "X":
                return
            
            visit.add((r, c))
            region.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i, j) not in visit:
                    dfs(i, j)
                    if not out_of_bounds:
                        for r, c in region:
                            board[r][c] = "X"

                    out_of_bounds = False
                    region.clear()



"""
Question:

You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
A surrounded region is captured by replacing all 'O's with 'X's in the input matrix board.

 

Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation:


In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:

Input: board = [["X"]]

Output: [["X"]]

 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
"""