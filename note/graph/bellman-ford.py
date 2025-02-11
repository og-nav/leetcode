from collections import *
from solutions.template import *

# bellman-ford
# given any starting node and a graph with positive and/or negative weights, returns the shortest distance from the 
# starting node to every other node in the graph
# Time Complexity: O(n * E)
# Space Complexity: O(n)

def bellman_ford(edges: List[List[int]], n: int, k: int):
  distances = {i: float('inf') for i in range(1, n + 1)}
  distances[k] = 0

  for _ in range(n - 1):
    for u, v, w in edges:
      if distances[u] + w < distances[v]: 
        distances[v] = distances[u] + w
  
  # perform check one more time to make sure there are no negative weight cycles
  # if any part of the graph changes now -> indicates a negative weight cycle
  for u, v, w in edges:
    if distances[u] + w < distances[v]:
      return -1 # negative cycle detected
  
  # finished
  # make sure to check for any infinities to see if any nodes weren't reached
  res = max(distances.values())
  return res if res != float('inf') else -1