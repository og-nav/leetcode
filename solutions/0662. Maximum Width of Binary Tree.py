"""
Title: Maximum Width of Binary Tree
URL: https://leetcode.com/problems/maximum-width-of-binary-tree/description/
Difficulty: Medium
Tags: Grind, Amazon, Bloomberg, Google, Meta, Apple
Topics: Tree
Depth-First Search
Breadth-First Search
Binary Tree

Approach:
- can do dfs or bfs
- just need to make sure to use the right indexing system
- if going left, 2 * difference
- if going right, 2 * difference + 1
- need to also remember that width is right - left + 1
- I tried using dummy null nodes as placeholders, but it gave memory limit exceeded error


Time Complexity: O(n)
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    # DFS
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        widths = defaultdict(list) # depth -> [left difference, right difference]
        res = 0

        def dfs(node, depth, difference):
            nonlocal res
            if not node:
                return
            if depth not in widths:
                widths[depth] = [difference, difference]
            else:
                widths[depth][0] = min(widths[depth][0], difference)
                widths[depth][1] = max(widths[depth][1], difference)
            
            res = max(res, widths[depth][1] - widths[depth][0] + 1)
            dfs(node.left, depth + 1, 2 * difference)
            dfs(node.right, depth + 1, 2 * difference + 1)
        
        dfs(root, 0, 0)
        return res

class Solution:
    # BFS
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        queue = deque([(root, 0)])
        while queue:
            res = max(res, queue[-1][1] - queue[0][1] + 1)
            for _ in range(len(queue)):
                node, diff = queue.popleft()

                if node.left:
                    queue.append((node.left, 2 * diff))
                if node.right:
                    queue.append((node.right, 2 * diff + 1))
        
        return res

"""
Question:

Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.

 

Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).
Example 2:


Input: root = [1,3,2,5,null,null,9,6,null,7]
Output: 7
Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).
Example 3:


Input: root = [1,3,2,5]
Output: 2
Explanation: The maximum width exists in the second level with length 2 (3,2).
 

Constraints:

The number of nodes in the tree is in the range [1, 3000].
-100 <= Node.val <= 100
"""