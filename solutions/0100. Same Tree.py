"""
Title: Same Tree
URL: https://leetcode.com/problems/same-tree/description/
Difficulty: Easy
Tags: NeetCode 150, Grind, Blind 75

Approach:
- first check if both are null -> return True
- elif check if one is null and other isn't
- elif check values

return left AND right


Time Complexity: O(n)
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif p and not q or not p and q:
            return False
        elif p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)



"""
Question:

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
"""