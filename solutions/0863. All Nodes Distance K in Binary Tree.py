"""
Title: All Nodes Distance K in Binary Tree
URL: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/
Difficulty: Medium
Tags: Grind, Meta, Amazon, Google, Walmart
Topics: Hash Table
Tree
Depth-First Search
Breadth-First Search
Binary Tree

Approach:
- convert to undirected graph
- BFS from target
- if distance == k, return list(queue)
- after BFS finishes, return []


Time Complexity: O(n)
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        def dfs(node):
            if not node:
                return
            
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
            
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        visit = set([target.val])
        queue = deque([target.val])
        distance = -1
        while queue:
            distance += 1
            if distance == k:
                return list(queue)

            for _ in range(len(queue)):
                node = queue.popleft()

                for neighbor in graph[node]:
                    if neighbor not in visit:
                        queue.append(neighbor)
                        visit.add(neighbor)

        return []



"""
Question:

Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
Example 2:

Input: root = [1], target = 1, k = 3
Output: []
 

Constraints:

The number of nodes in the tree is in the range [1, 500].
0 <= Node.val <= 500
All the values Node.val are unique.
target is the value of one of the nodes in the tree.
0 <= k <= 1000
"""