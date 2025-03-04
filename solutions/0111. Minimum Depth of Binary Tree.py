"""
Title: Minimum Depth of Binary Tree
URL: https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
Difficulty: Easy
Tags: Meta, Amazon, Microsoft, Apple, Bloomberg, Google
Topics: Tree
Depth-First Search
Breadth-First Search
Binary Tree

Approach:
- do bfs since it will break faster on average


Time Complexity: O(n)
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([root])
        height = 0
        while queue:
            height += 1
            for _ in range(len(queue)):
                node = queue.popleft()

                if not node.left and not node.right:
                    return height

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return -1



"""
Question:

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
 

Constraints:

The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000
"""