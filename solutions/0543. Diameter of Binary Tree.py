"""
Title: Diameter of Binary Tree
URL: https://leetcode.com/problems/diameter-of-binary-tree/description/
Difficulty: Easy
Tags: NeetCode 150, Grind, Meta, Amazon, Google, Apple, Bloomberg, Microsoft
Topics: Tree
Depth-First Search
Binary Tree

Approach:
- need to do post order 
- think about what if the tree was just a root or a root and two children and use that to figure it out
- tbh, just memorize the idea. the same idea is also used in 124. Binary Tree Maximum Path Sum
-- so study in depth before interview


Time Complexity: O(n)
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            
            left_path = dfs(node.left)
            right_path = dfs(node.right)
            res = max(res, left_path + right_path)

            return max(left_path, right_path) + 1
        
        dfs(root)
        return res



"""
Question:

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 

Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
"""