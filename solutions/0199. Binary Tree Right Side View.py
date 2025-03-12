"""
Title: Binary Tree Right Side View
URL: https://leetcode.com/problems/binary-tree-right-side-view/description/
Difficulty: Medium
Tags: NeetCode 150, Grind, Meta, Amazon, TikTok, Google, Bloomberg
Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree

Approach:
- stock BFS
- append last element of queue in time/level spot to result
- simple


Time Complexity: O(n)
Space Complexity: O(n) -> complete binary tree contains n / 2 nodes on last level



Solution:
"""
from template import *

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        res = []
        queue = deque([root])
        while queue:
            res.append(queue[-1].val)
            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return res



"""
Question:

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""