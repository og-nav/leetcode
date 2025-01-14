"""
Title: Range Sum of BST
URL: https://leetcode.com/problems/range-sum-of-bst/description/
Difficulty: Easy
Tags: Meta

Approach:
- just regular (iterative or recursive) dfs and add value to result variable
- no way to utilize property of BST, but you could bring up inorder traversal


Time Complexity: O(n)
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if low <= node.val and node.val <= high:
                res += node.val
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return res



"""
Question:

Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

 

Example 1:


Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
Example 2:


Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
 

Constraints:

The number of nodes in the tree is in the range [1, 2 * 104].
1 <= Node.val <= 105
1 <= low <= high <= 105
All Node.val are unique.
"""