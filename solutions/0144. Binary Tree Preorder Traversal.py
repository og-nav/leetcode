"""
Title: Binary Tree Preorder Traversal
URL: https://leetcode.com/problems/binary-tree-preorder-traversal/description/
Difficulty: Easy
Tags: 

Approach:
- helper dfs function, add before calling dfs
- iterative: pretty much how you would do recursive but in iterative form
- NOTE: YOU NEED TO ADD THE RIGHT NODE FIRST AND THEN THE LEFT NODE BECAUSE THE LEFT NODE NEEDS TO GET POPPED FIRST


Time Complexity: O(n)
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        def dfs(node):
            if not node:
                return
            
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
    
        dfs(root)
        return res

    def preorderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return res


"""
Question:

Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,2,3]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up: Recursive solution is trivial, could you do it iteratively?
"""