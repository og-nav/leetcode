"""
Title: Game of Life
URL: https://leetcode.com/problems/game-of-life/description/
Difficulty: Medium
Tags: Salesforce, Google, Microsoft, Amazon, Meta
Topics: String, Stack, etc

Approach:
- need a scheme to mark a cell is alive and dies or is dead and comes back
- make sure not to get caught up in muscle memory and type wrong variable names like grid or r + dr


Time Complexity: O(m * n)
Space Complexity: O(1)



Solution:
"""
from template import *

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 0 dead
        # 1 alive
        # 2 dead -> alive
        # 3 alive -> dead
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, -1], [1, 1], [-1, 1], [1, -1]]
        def invalid(r, c):
            return r < 0 or c < 0 or r >= len(board) or c >= len(board[0])
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                alive = 0
                for dr, dc in directions:
                    if invalid(r + dr, c + dc):
                        continue
                    
                    alive += board[r + dr][c + dc] % 2
                
                if board[r][c] == 1:
                    if alive < 2 or alive > 3:
                        board[r][c] = 3
                else:
                    if alive == 3:
                        board[r][c] = 2

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 3:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1



"""
Question:

According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.

Given the current state of the board, update the board to reflect its next state.

Note that you do not need to return anything.

 

Example 1:


Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
Example 2:


Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.
 

Follow up:

Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?
"""