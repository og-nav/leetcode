"""
Title: Network Delay Time
URL: https://leetcode.com/problems/network-delay-time/description/
Difficulty: Medium
Tags: NeetCode 150
Topics: Depth-First Search Breadth-First Search Graph Heap (Priority Queue) Shortest Path

Approach:
- Basically Dijkstra's, but we take the longest path
- Dijkstra's is basically regular graph BFS but with a minHeap instead of a queue
- keep track of visited nodes in the set, and set res to whenever we encounter a node for the first time
- initial weight is 0, and as you add nodes to the heap, do weight + w
- IMPORTANT: make sure the first element in the tuple is the weight and NOT the node


Time Complexity: O(V + E log(V))
Space Complexity: O(V + E)



Solution:
"""
from template import *
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
  
        visit = set()
        minHeap = [(0, k)]
        heapq.heapify(minHeap)
        res = 0
        while minHeap:
            w, u = heapq.heappop(minHeap)
            if u not in visit:
                visit.add(u)
                res = w

                for neighbor, weight in graph[u]:
                    if neighbor not in visit:
                        heapq.heappush(minHeap, (weight + w, neighbor))

        if len(visit) == n:
            return res
        return -1
              

"""
Question:

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

 

Example 1:


Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
 

Constraints:

1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
"""