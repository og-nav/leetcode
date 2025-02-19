"""
Title: Maximum Level Sum of a Binary Tree
URL: https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/
Difficulty: Medium
Tags: Meta, Google, Amazon, Microsoft, Adobe, Apple
Topics: Tree
Depth-First Search
Breadth-First Search
Binary Tree

Approach:
- just bfs with some caveats
- however, caveats are very important
- read question carefully - easy to assume and start solving the wrong problem
-- especially with variable naming. might be best avoid res this time


Time Complexity: O(n)
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_level_sum = root.val
        res = 1
        current_level = 0
        queue = deque([root])
        while queue:
            level_sum = 0
            current_level += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if level_sum > max_level_sum:
                res = current_level
                max_level_sum = level_sum

        return res



"""
Question:

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 

Example 1:


Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
"""