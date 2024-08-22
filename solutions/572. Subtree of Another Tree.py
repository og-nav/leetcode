"""
Title: Subtree of Another Tree
URL: https://leetcode.com/problems/subtree-of-another-tree/description/
Difficulty: Easy
Tags: NeetCode 150, Grind, Blind 75

Approach:
- helper function to check if same tree
- brute force
- chose to do iterative for main traversal to avoid double dfs


Time Complexity: O(n * m)
Space Complexity: O(n + m)



Solution:
"""
from template import *

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(p, q):
            if not p and not q:
                return True
            elif p and not q or not p and q:
                return False
            elif p.val != q.val:
                return False

            return sameTree(p.left, q.left) and sameTree(p.right, q.right)
        
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val == subRoot.val:
                if sameTree(node, subRoot):
                    return True
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return False



"""
Question:

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
 

Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104
"""