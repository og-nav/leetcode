"""
Title: Count Good Nodes in Binary Tree
URL: https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/
Difficulty: Medium
Tags: NeetCode 150, Meta, Microsoft, Google, Amazon
Topics: Tree
Depth-First Search
Breadth-First Search
Binary Tree

Approach:
- just keep track of the current maximum value along the path
-- if current node is greater, then update it accordingly and increment result


Time Complexity: O(n)
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(node, curr_max):
            nonlocal res
            if not node:
                return
            
            if node.val >= curr_max:
                res += 1
                curr_max = node.val
            
            dfs(node.left, curr_max)
            dfs(node.right, curr_max)
        
        dfs(root, root.val)
        return res



"""
Question:

Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

 

Example 1:



Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
Example 2:



Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.
 

Constraints:

The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].
"""