"""
Title: Find Largest Value in Each Tree Row
URL: https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/
Difficulty: Medium
Tags: Meta, Amazon, Bloomberg, Adobe
Topics: Tree
Depth-First Search
Breadth-First Search
Binary Tree

Approach:
- most straightforward is to do bfs and do max of each row
- optimization where before inner for loop you save max and update max within the for loop
- can also do dfs


Time Complexity: O(n)
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        queue = deque([root])
        while queue:
            max_val = queue[0].val
            for _ in range(len(queue)):
                node = queue.popleft()
                max_val = max(max_val, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(max_val)
        
        return res



"""
Question:

Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

 

Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
Example 2:

Input: root = [1,2,3]
Output: [1,3]
 

Constraints:

The number of nodes in the tree will be in the range [0, 104].
-231 <= Node.val <= 231 - 1
"""