"""
Title: Reorder Routes to Make All Paths Lead to the City Zero
URL: https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/
Difficulty: Medium
Tags: Microsoft, Amazon, TikTok
Topics: Depth-First Search
Breadth-First Search
Graph

Approach:
- just create an undirected version of the cities
- then do bfs starting from 0
- any time you bfs over an edge that isn't in the original connections list, we know we need to reverse it
- just make sure to subtract one at the end because (0, 0) isn't in connections but will be added to res


Time Complexity: O(n)
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        edges = set()
        for u, v in connections:
            edges.add((u, v))
            graph[u].append(v)
            graph[v].append(u)
        
        res = 0
        visit = set([0])
        queue = deque([(0, 0)]) # (node, prev)
        while queue:
            for _ in range(len(queue)):
                node, prev = queue.popleft()

                if (node, prev) not in edges:
                    # this edge needs to be reversed
                    res += 1
                
                for neighbor in graph[node]:
                    if neighbor not in visit:
                        visit.add((neighbor))
                        queue.append((neighbor, node))
        
        return res - 1



"""
Question:


"""