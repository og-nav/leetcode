"""
Title: Pseudo-Palindromic Paths in a Binary Tree
URL: https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/description/
Difficulty: Medium
Tags: 
Topics: Bit Manipulation
Tree
Depth-First Search
Breadth-First Search
Binary Tree
Backtracking

Approach:
- pseudo-palindromic means at most 1 odd count in counts list
- we do stock dfs with helper function that checks pseudo-palindromic
- need backtracking step at the end


Time Complexity: O(n)
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        res = 0
        def is_pseudo_palindromic(counts):
            num_odd = 0
            for count in counts:
                if count % 2 == 1:
                    num_odd += 1
                if num_odd > 1:
                    return False
            
            return True

        def dfs(node, counts):
            nonlocal res
            if not node:
                return
            
            counts[node.val] += 1
            if is_pseudo_palindromic(counts) and not node.left and not node.right:
                res += 1
            
            dfs(node.left, counts)
            dfs(node.right, counts)
            counts[node.val] -= 1
        
        dfs(root, [0 for _ in range(10)])
        return res



"""
Question:

Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

 

Example 1:



Input: root = [2,3,1,3,1,null,1]
Output: 2 
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).
Example 2:



Input: root = [2,1,1,1,3,null,null,null,null,null,1]
Output: 1 
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).
Example 3:

Input: root = [9]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [1, 105].
1 <= Node.val <= 9
"""