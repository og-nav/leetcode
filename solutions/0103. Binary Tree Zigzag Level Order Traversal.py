"""
Title: Binary Tree Zigzag Level Order Traversal
URL: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
Difficulty: Medium
Tags: Grind

Approach:
- standard BFS
- note: keep a direction variable that multiplies by -1 each queue iteration to get which direction the row should be appended as


Time Complexity: O(n)
Space Complexity: O(n) -> queue holds two levels 
                          num of leaf nodes of full binary tree is roughly n / 2
                          two levels * n / 2 = n



Solution:
"""
from template import *

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        queue = deque([root])
        direction = -1
        while queue:
            row = []
            direction *= -1
            for _ in range(len(queue)):
                node = queue.popleft()
                row.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if direction == -1:
                res.append(row[::-1])
            else:
                res.append(row)
        
        return res



"""
Question:

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
"""