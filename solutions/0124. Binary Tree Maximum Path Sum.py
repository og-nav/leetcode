"""
Title: Binary Tree Maximum Path Sum
URL: https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
Difficulty: Hard
Tags: NeetCode 150, Grind, Blind 75, Meta, Google, Amazon, Apple, DoorDash
Topics: Dynamic Programming
Tree
Depth-First Search
Binary Tree

Approach:
- requires some convoluted thinking. did not fully understand, so make sure to revise.
- also solve:
-- 543. Diameter of Binary Tree
-- 687. Longest Univalue Path
-- 2265. Count Nodes Equal to Average of Subtree
- for similar post-order ideas


Time Complexity: O(n)
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)
            current_gain = node.val + left_gain + right_gain
            res = max(res, current_gain)

            return node.val + max(left_gain, right_gain)
        
        dfs(root)
        return res



"""
Question:

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 

Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000

"""