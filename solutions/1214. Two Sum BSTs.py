"""
Title: Two Sum BSTs
URL: https://leetcode.com/problems/two-sum-bsts/description/
Difficulty: Medium
Tags: Amazon
Topics: Two Pointers
Binary Search
Stack
Tree
Depth-First Search
Binary Search Tree
Binary Tree

Approach:
- the fact the problem has BSTs is deceptive
- since we will have to anyways compare each value to each value since there are negative numbers
- so use two sum complement approach
- you can do iterative approach for quick return if match is found


Time Complexity: O(m + n)
Space Complexity: O(m + n)



Solution:
"""
from template import *

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        complement = set()
        def dfs(node):
            if not node:
                return
            
            complement.add(target - node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root1)
        
        stack = [root2]
        while stack:
            node = stack.pop()
            if node.val in complement:
                return True
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return False



"""
Question:

Given the roots of two binary search trees, root1 and root2, return true if and only if there is a node in the first tree and a node in the second tree whose values sum up to a given integer target.

 

Example 1:


Input: root1 = [2,1,4], root2 = [1,0,3], target = 5
Output: true
Explanation: 2 and 3 sum up to 5.
Example 2:


Input: root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
Output: false
 

Constraints:

The number of nodes in each tree is in the range [1, 5000].
-109 <= Node.val, target <= 109
"""