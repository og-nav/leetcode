"""
Title: Count Servers that Communicate
URL: https://leetcode.com/problems/count-servers-that-communicate/description/
Difficulty: Medium
Tags: Google, Amazon, Bloomberg, Meta, Microsoft, Oracle
Topics: Array
Depth-First Search
Breadth-First Search
Union Find
Matrix
Counting

Approach:
- simple to understand, but easy to overthink
- we just need to have a frequency counter for each row and col
-- i.e. iterate through the grid and each time you encounter a server, increase its rows and cols by 1
- I got mentally blocked on this last part. instead of trying to go by each server and checking the rows and cols,
-- instead just iterate through the array normally. once you encounter a server, just check the count of the its
-- row and col to make sure its more than 1 in either one.
-- I got messed up because I was worried about double counting a server and potentially needing to do some kind of 
-- math formula to not double count, but just iterating through the grid normally means that each server is only
-- visited and counted once.


Time Complexity: O(m * n)
Space Complexity: O(m + n)



Solution:
"""
from template import *

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = [0 for _ in range(len(grid))]
        cols = [0 for _ in range(len(grid[0]))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if rows[i] > 1 or cols[j] > 1:
                        res += 1
        
        return res



"""
Question:

You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.

 

Example 1:



Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.
Example 2:



Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.
Example 3:



Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m <= 250
1 <= n <= 250
grid[i][j] == 0 or 1
"""