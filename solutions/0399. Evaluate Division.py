"""
Title: Evaluate Division
URL: https://leetcode.com/problems/evaluate-division/description/
Difficulty: Medium
Tags: Bloomberg, Amazon, BlackRock, Google, Meta, Microsoft
Topics: Array
String
Depth-First Search
Breadth-First Search
Union Find
Graph
Shortest Path

Approach:
- standard graph problem
- since graph is directed, save u -> v with regular weight and then v -> u with 1 / weight in case we need
- then we can do dfs or bfs. iterative stack allows you to use while else instead of creating a boolean found flag
- don't forget to check if the node exists in the graph before starting dfs/bfs
- also a variant could use currency exchanges with the rate


Time Complexity: O(m * n) -> m queries and n graph nodes to process
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i, (u, v) in enumerate(equations):
            graph[u].append((v, values[i]))
            graph[v].append((u, 1 / values[i]))
        
        res = []
        for u, v in queries:
            if u not in graph or v not in graph:
                res.append(-1)
                continue
            
            stack = [(u, 1)] # (start node, product)
            visit = set()
            while stack:
                node, product = stack.pop()
                if node in visit:
                    continue

                if node == v:
                    res.append(product)
                    break
                
                visit.add(node)
                for (neighbor, value) in graph[node]:
                    stack.append((neighbor, product * value))
            else:
                res.append(-1)
        
        return res


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i, (u, v) in enumerate(equations):
            graph[u].append((v, values[i]))
            graph[v].append((u, 1 / values[i]))
        
        res = []
        for u, v in queries:
            queue = deque([(u, 1)]) # (starting node, product)
            visit = set([u])
            found = False
            while queue:
                for _ in range(len(queue)):
                    node, product = queue.popleft()

                    if node not in graph:
                        queue.clear()
                        break

                    if node == v:
                        res.append(product)
                        queue.clear()
                        found = True
                        break
                    
                    for (neighbor, value) in graph[node]:
                        if neighbor not in visit:
                            queue.append((neighbor, product * value))
                            visit.add(neighbor)
            
            if not found:
                res.append(-1)
        
        return res

"""
Question:

You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

 

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0
Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
 

Constraints:

1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.
"""