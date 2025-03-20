"""
Title: Binary Tree Vertical Order Traversal
URL: https://leetcode.com/problems/binary-tree-vertical-order-traversal/description/
Difficulty: Medium
Tags: Meta, Bloomberg, Amazon, Google, Microsoft, Apple, TikTok
Topics: Hash Table
Tree
Depth-First Search
Breadth-First Search
Sorting
Binary Tree

Approach:
- putting all nodes into an array and sorting using key=lambda x: x[0] is the naive way
- optimal way is to use BFS and just save the left-most and right-most columns
- since bfs will already go left to right and preserve the order
- then we can just iterate through left, right + 1 and use list comprehension to build the result


Time Complexity: O(n)
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        columns = defaultdict(list)
        min_column = float('inf')
        max_column = float('-inf')
        queue = deque([(root, 0)]) # (node, column)
        while queue:
            for _ in range(len(queue)):
                node, column = queue.popleft()
                columns[column].append(node.val)
                min_column = min(min_column, column)
                max_column = max(max_column, column)

                if node.left:
                    queue.append((node.left, column - 1))
                if node.right:
                    queue.append((node.right, column + 1))
        
        return [columns[i] for i in range(min_column, max_column + 1)]



"""
Question:

Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Example 2:


Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]
Example 3:


Input: root = [1,2,3,4,10,9,11,null,5,null,null,null,null,null,null,null,6]
Output: [[4],[2,5],[1,10,9,6],[3],[11]]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""