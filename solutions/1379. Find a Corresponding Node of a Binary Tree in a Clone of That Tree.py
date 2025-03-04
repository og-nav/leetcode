"""
Title: Find a Corresponding Node of a Binary Tree in a Clone of That Tree
URL: https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/description/
Difficulty: Easy
Tags: Meta, Amazon, Bloomberg
Topics: Tree
Depth-First Search
Breadth-First Search
Binary Tree

Approach:
- if trees have unique values, simple dfs is easy
- if trees have duplicate values, simply run bfs in parallel until you find the match


Time Complexity: O(n)
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        queue = deque([(original, cloned)])
        while queue:
            for _ in range(len(queue)):
                o_node, c_node = queue.popleft()

                if o_node == target:
                    return c_node
                
                if o_node.left:
                    queue.append((o_node.left, c_node.left))
                if o_node.right:
                    queue.append((o_node.right, c_node.right))
        
        return None



"""
Question:

Given two binary trees original and cloned and given a reference to a node target in the original tree.

The cloned tree is a copy of the original tree.

Return a reference to the same node in the cloned tree.

Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.

 

Example 1:


Input: tree = [7,4,3,null,null,6,19], target = 3
Output: 3
Explanation: In all examples the original and cloned trees are shown. The target node is a green node from the original tree. The answer is the yellow node from the cloned tree.
Example 2:


Input: tree = [7], target =  7
Output: 7
Example 3:


Input: tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4
Output: 4
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
The values of the nodes of the tree are unique.
target node is a node from the original tree and is not null.
 

Follow up: Could you solve the problem if repeated values on the tree are allowed?
"""