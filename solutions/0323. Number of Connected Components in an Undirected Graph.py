"""
Title: Number of Connected Components in an Undirected Graph
URL: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/
Difficulty: Medium
Tags: NeetCode 150, Grind, Blind 75, Meta, General Motors, LinkedIn, Amazon, Google, TikTok
Topics: Depth-First Search
Breadth-First Search
Union Find
Graph

Approach:
- dfs or bfs on non-visited nodes


Time Complexity: O(V + E)
Space Complexity: O(V + E)



Solution:
"""
from template import *

# BFS
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visit = set()
        for i in range(n):
            if i in visit:
                continue
            
            res += 1
            queue = deque([i])
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    
                    for neighbor in graph[node]:
                        if neighbor not in visit:
                            visit.add(neighbor)
                            queue.append(neighbor)
        
        return res
                

# DFS
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visit = set()
        def dfs(node):
            if node in visit:
                return
            
            visit.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)

        
        res = 0
        for i in range(n):
            if i not in visit:
                res += 1
                dfs(i)
        
        return res



"""
Question:

You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

 

Example 1:


Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
Example 2:


Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1
 

Constraints:

1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= ai <= bi < n
ai != bi
There are no repeated edges.
"""