"""
Title: Sum of Root To Leaf Binary Numbers
URL: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/description/
Difficulty: Easy
Tags: Microsoft, Amazon
Topics: Tree
Depth-First Search
Binary Tree

Approach:
- need bitwise trick where you shift to the left by 1 position and then add the current node's value


Time Complexity: O(n)
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node, curr_sum):
            nonlocal res
            if not node:
                return
            
            curr_sum <<= 1
            curr_sum += node.val

            if not node.left and not node.right:
                res += curr_sum
            
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
        
        dfs(root, 0)
        return res



"""
Question:

You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.

For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.

The test cases are generated so that the answer fits in a 32-bits integer.

 

Example 1:


Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
Example 2:

Input: root = [0]
Output: 0
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
Node.val is 0 or 1.
"""