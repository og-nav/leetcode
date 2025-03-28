"""
Title: Find the Closest Marked Node
URL: https://leetcode.com/problems/find-the-closest-marked-node/description/
Difficulty: Medium
Tags: None
Topics: Array
Graph
Heap (Priority Queue)
Shortest Path

Approach:
- straight up dijkstra's
- convert marked to a set and since dijkstra's is greedy, the first time we encounter a node in marked is the correct answer


Time Complexity: O((m + n)log(n))
Space Complexity: O(m + n)



Solution:
"""
from template import *

class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        marked = set(marked)
        graph = defaultdict(list)
        visit = set()
        for u, v, w in edges:
            if (u, v, w) not in visit:
                graph[u].append((v, w))
        
        distances = {i: float('inf') for i in range(n)}
        distances[s] = 0
        heap = [(0, s)] # current_distance, node
        while heap:
            current_distance, node = heapq.heappop(heap)

            if node in marked:
                return current_distance

            # node was seen before and pushed to the heap multiple times
            if current_distance > distances[node]:
                continue
            
            for neighbor, distance in graph[node]:
                new_distance = current_distance + distance
                if new_distance < distances[neighbor]:
                    heapq.heappush(heap, (new_distance, neighbor))
                    distances[neighbor] = new_distance
        
        return -1



"""
Question:

You are given a positive integer n which is the number of nodes of a 0-indexed directed weighted graph and a 0-indexed 2D array edges where edges[i] = [ui, vi, wi] indicates that there is an edge from node ui to node vi with weight wi.

You are also given a node s and a node array marked; your task is to find the minimum distance from s to any of the nodes in marked.

Return an integer denoting the minimum distance from s to any node in marked or -1 if there are no paths from s to any of the marked nodes.

 

Example 1:

Input: n = 4, edges = [[0,1,1],[1,2,3],[2,3,2],[0,3,4]], s = 0, marked = [2,3]
Output: 4
Explanation: There is one path from node 0 (the green node) to node 2 (a red node), which is 0->1->2, and has a distance of 1 + 3 = 4.
There are two paths from node 0 to node 3 (a red node), which are 0->1->2->3 and 0->3, the first one has a distance of 1 + 3 + 2 = 6 and the second one has a distance of 4.
The minimum of them is 4.


Example 2:

Input: n = 5, edges = [[0,1,2],[0,2,4],[1,3,1],[2,3,3],[3,4,2]], s = 1, marked = [0,4]
Output: 3
Explanation: There are no paths from node 1 (the green node) to node 0 (a red node).
There is one path from node 1 to node 4 (a red node), which is 1->3->4, and has a distance of 1 + 2 = 3.
So the answer is 3.


Example 3:

Input: n = 4, edges = [[0,1,1],[1,2,3],[2,3,2]], s = 3, marked = [0,1]
Output: -1
Explanation: There are no paths from node 3 (the green node) to any of the marked nodes (the red nodes), so the answer is -1.


 

Constraints:

2 <= n <= 500
1 <= edges.length <= 104
edges[i].length = 3
0 <= edges[i][0], edges[i][1] <= n - 1
1 <= edges[i][2] <= 106
1 <= marked.length <= n - 1
0 <= s, marked[i] <= n - 1
s != marked[i]
marked[i] != marked[j] for every i != j
The graph might have repeated edges.
The graph is generated such that it has no self-loops.
"""