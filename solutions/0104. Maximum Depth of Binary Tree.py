"""
Title: Maximum Depth of Binary Tree
URL: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
Difficulty: Easy
Tags: NeetCode 150, Grind, Blind 75

Approach:
- dfs function with depth as parameter
- make sure to check for null root initially


Time Complexity: O(n)
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        res = 0
        def dfs(node, depth):
            nonlocal res
            if not node:
                return
            
            res = max(res, depth)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
            
        dfs(root, 1)
        return res



"""
Question:

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""