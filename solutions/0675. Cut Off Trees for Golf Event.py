"""
Title: Cut Off Trees for Golf Event
URL: https://leetcode.com/problems/cut-off-trees-for-golf-event/description/
Difficulty: Hard
Tags: Amazon, Google
Topics: Array
Breadth-First Search
Heap (Priority Queue)
Matrix

Approach:
- brute force bfs
- use heap to sort everything, or just regular sort tbh
- then do bfs from origin to smallest tree, then do bfs from smallest tree to second smallest tree, etc
-- until heap is empty (or all trees are cut)
- once target square is reached, reset queue, add to result, modify grid value to 1, update current position, then
-- update progress flag
- return -1 if no progress (a tree is cut) is made after a bfs


Time Complexity: O((m * n) ^ 2)
Space Complexity: O(m * n)



Solution:
"""
from template import *

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        heap = [] # min heap
        for i in range(len(forest)):
            for j in range(len(forest[0])):
                if forest[i][j] > 1:
                    heapq.heappush(heap, (forest[i][j], i, j))
        
        def invalid(r, c):
            return r < 0 or c < 0 or r >= len(forest) or c >= len(forest[0])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        current_r, current_c = 0, 0
        res = 0
        while heap:
            queue = deque([(current_r, current_c)])
            visit = set([current_r, current_c])
            steps = -1
            _, target_r, target_c = heapq.heappop(heap)
            progress = False
            while queue:
                steps += 1
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    if r == target_r and c == target_c:
                        queue = deque([])
                        res += steps
                        forest[r][c] = 1
                        current_r, current_c = r, c
                        progress = True
                        break
                    
                    for dr, dc in directions:
                        if not invalid(r + dr, c + dc) and (r + dr, c + dc) not in visit and forest[r + dr][c + dc] >= 1:
                            queue.append((r + dr, c + dc))
                            visit.add((r + dr, c + dc))

            if not progress:
                return -1
            progress = False
                
        return res


"""
Question:

You are asked to cut off all the trees in a forest for a golf event. The forest is represented as an m x n matrix. In this matrix:

0 means the cell cannot be walked through.
1 represents an empty cell that can be walked through.
A number greater than 1 represents a tree in a cell that can be walked through, and this number is the tree's height.
In one step, you can walk in any of the four directions: north, east, south, and west. If you are standing in a cell with a tree, you can choose whether to cut it off.

You must cut off the trees in order from shortest to tallest. When you cut off a tree, the value at its cell becomes 1 (an empty cell).

Starting from the point (0, 0), return the minimum steps you need to walk to cut off all the trees. If you cannot cut off all the trees, return -1.

Note: The input is generated such that no two trees have the same height, and there is at least one tree needs to be cut off.

 

Example 1:


Input: forest = [[1,2,3],[0,0,4],[7,6,5]]
Output: 6
Explanation: Following the path above allows you to cut off the trees from shortest to tallest in 6 steps.
Example 2:


Input: forest = [[1,2,3],[0,0,0],[7,6,5]]
Output: -1
Explanation: The trees in the bottom row cannot be accessed as the middle row is blocked.
Example 3:

Input: forest = [[2,3,4],[0,0,5],[8,7,6]]
Output: 6
Explanation: You can follow the same path as Example 1 to cut off all the trees.
Note that you can cut off the first tree at (0, 0) before making any steps.
 

Constraints:

m == forest.length
n == forest[i].length
1 <= m, n <= 50
0 <= forest[i][j] <= 109
Heights of all trees are distinct.
"""