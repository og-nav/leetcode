"""
Title: Graph Valid Tree
URL: https://leetcode.com/problems/graph-valid-tree/description/
Difficulty: Medium
Tags: NeetCode 150, Grind, Blind 75, Google, Amazon, Meta, Snowflake, Microsoft, Salesforce
Topics: Depth-First Search
Breadth-First Search
Union Find
Graph

Approach:
- need to understand graph vs tree properties
- tree has n - 1 edges
- graph with less than n - 1 edges is definitely not connected
- graph with more than n - 1 edges definitely has a cycle
- therefore, we first just check that the number of edges is equal to n - 1
- then we can just do a basic bfs
- then we just need to make sure all nodes were visited
- can start bfs at any node


Time Complexity: O(n + e) -> iterate through all edges for adjacency list and then n nodes
Space Complexity: O(n + e) -> adjacency list holds all edges and then n nodes in visit set



Solution:
"""
from template import *

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visit = set([0])
        queue = deque([0])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                for neighbor in graph[node]:
                    if neighbor not in visit:
                        visit.add((neighbor))
                        queue.append(neighbor)
        
        return len(visit) == n



"""
Question:

You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.

 

Example 1:


Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
Example 2:


Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
 

Constraints:

1 <= n <= 2000
0 <= edges.length <= 5000
edges[i].length == 2
0 <= ai, bi < n
ai != bi
There are no self-loops or repeated edges.
"""