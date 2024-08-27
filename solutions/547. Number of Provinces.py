"""
Title: Number of Provinces
URL: https://leetcode.com/problems/number-of-provinces/description/
Difficulty: Medium
Tags: 
Topics: Depth-First Search
Breadth-First Search
Union Find
Graph

Approach:
- very Number of Islands-esque style to it
- convert adjacency list to graph
- have a global visit since we only need to visit each city once
- iterate through all cities
- if city in visit, we continue
- else, res += 1 and bfs the province


Time Complexity: O(n * n)
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if i != j and isConnected[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)

        res = 0
        visit = set()
        for i in range(len(isConnected)):
            if i in visit:
                continue
            
            res += 1
            queue = deque([i])
            visit.add(i)
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()

                    for neighbor in graph[node]:
                        if neighbor not in visit:
                            queue.append(neighbor)
                            visit.add(neighbor)
        
        return res

        



"""
Question:

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

 

Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
 

Constraints:

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
"""