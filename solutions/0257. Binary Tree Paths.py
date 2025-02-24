"""
Title: Binary Tree Paths
URL: https://leetcode.com/problems/binary-tree-paths/description/
Difficulty: Easy
Tags: Meta, Google, Apple, Amazon, Bloomberg, Microsoft
Topics: String, Stack, etc

Approach:
- regular dfs with a path array
- make sure to use backtracking and not string builder since string builder will tend to O(n ^ 2) time complexity
- also make sure to append string to the path instead of int per the "".join stuff


Time Complexity: O(n)
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def dfs(node, path):
            if not node:
                return
            
            path.append(str(node.val))
            if not node.left and not node.right:
                res.append("->".join(path))
            
            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()
        
        dfs(root, [])
        return res



"""
Question:

Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

 

Example 1:


Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
Example 2:

Input: root = [1]
Output: ["1"]
 

Constraints:

The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100
"""