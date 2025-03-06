"""
Title: Univalued Binary Tree
URL: https://leetcode.com/problems/univalued-binary-tree/description/
Difficulty: Easy
Tags: None
Topics: Tree
Depth-First Search
Breadth-First Search
Binary Tree

Approach:
- iterative stack so we can return early

Time Complexity: O(n)
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        univalue = root.val
        stack = [root]
        while stack:
            node = stack.pop()

            if node.val != univalue:
                return False
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return True



"""
Question:

A binary tree is uni-valued if every node in the tree has the same value.

Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.

 

Example 1:


Input: root = [1,1,1,1,1,null,1]
Output: true
Example 2:


Input: root = [2,2,2,5,2]
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 100].
0 <= Node.val < 100
"""