"""
Title: Binary Tree Postorder Traversal
URL: https://leetcode.com/problems/binary-tree-postorder-traversal/description/
Difficulty: Easy
Tags: 

Approach:
- dfs helper function
- append to res after calling dfs on left and right

- iterative solution
- basically just preorder but reversed
- and you do preorder analogous to regular dfs, just with iterative stack

Time Complexity: O(n)
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
        
        dfs(root)
        return res


    def postorderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return res[::-1]



"""
Question:

Given the root of a binary tree, return the postorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [3,2,1]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
 

Constraints:

The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up: Recursive solution is trivial, could you do it iteratively?
"""