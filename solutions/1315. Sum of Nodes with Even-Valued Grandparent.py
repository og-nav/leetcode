"""
Title: Sum of Nodes with Even-Valued Grandparent
URL: https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/description/
Difficulty: Medium
Tags: Salesforce, Meta, Amazon
Topics: Tree
Depth-First Search
Breadth-First Search
Binary Tree

Approach:
- can just do regular dfs but pass in parent and grandparent for each node


Time Complexity: O(n)
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node, parent, grandparent):
            nonlocal res
            if not node:
                return
            
            if grandparent and grandparent.val % 2 == 0:
                res += node.val

            if node.left:
                dfs(node.left, node, parent)
            
            if node.right:
                dfs(node.right, node, parent)
        
        dfs(root, None, None)
        return res



"""
Question:

Given the root of a binary tree, return the sum of values of nodes with an even-valued grandparent. If there are no nodes with an even-valued grandparent, return 0.

A grandparent of a node is the parent of its parent if it exists.

 

Example 1:


Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
Example 2:


Input: root = [1]
Output: 0
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 100
"""