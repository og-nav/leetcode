"""
Title: Path Sum
URL: https://leetcode.com/problems/path-sum/description/
Difficulty: Easy
Tags: Amazon, Meta, Microsoft, Google, Bloomberg
Topics: Tree
Depth-First Search
Breadth-First Search
Binary Tree

Approach:
- use iterative to return early


Time Complexity: O(n)
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        stack = [(root, 0)] # (node, path_sum)
        while stack:
            node, path_sum = stack.pop()
            path_sum += node.val

            if not node.left and not node.right and path_sum == targetSum:
                return True
            
            if node.left:
                stack.append((node.left, path_sum))
            if node.right:
                stack.append((node.right, path_sum))
        
        return False



"""
Question:

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

 

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There are two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.
Example 3:

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""