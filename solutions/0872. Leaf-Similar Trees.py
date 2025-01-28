"""
Title: Leaf-Similar Trees
URL: https://leetcode.com/problems/leaf-similar-trees/description/
Difficulty: Easy
Tags: Snowflake, Amazon, Adobe, Google, Meta, Microsoft, Apple
Topics: Tree
Depth-First Search
Binary Tree

Approach:
- dfs the leaves of both trees into their own arrays
- use preorder traversal for both
- check if leaves arrays are equal


Time Complexity: O(m + n)
Space Complexity: O(m + n)



Solution:
"""
from template import *

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        root1_leaves = []
        root2_leaves = []

        def dfs(node, is_root1):
            if not node:
                return
            
            if not node.left and not node.right:
                if is_root1:
                    root1_leaves.append(node.val)
                else:
                    root2_leaves.append(node.val)
            
            dfs(node.left, is_root1)
            dfs(node.right, is_root1)
        
        dfs(root1, True)
        dfs(root2, False)
        return root1_leaves == root2_leaves



"""
Question:

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

Example 1:


Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
Example 2:


Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false
 

Constraints:

The number of nodes in each tree will be in the range [1, 200].
Both of the given trees will have values in the range [0, 200].
"""