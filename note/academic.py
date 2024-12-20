from collections import *
import heapq

# dijkstra's algorithm
# given any starting node and a graph with positive weights, returns the shortest distance from the 
# starting node to every other node in the graph
# Time Complexity: O(V + E log(V))
# Space Complexity: O(V + E)

def dijkstra(edges: List[List[int]], n: int, k: int):
  # edges[i] = (u, v, w) -> (source, destination, weight)
  # n is the number of nodes
  # k is the starting node

  # convert edge list w/ weights to usable form
  graph = defaultdict(list)
  for u, v, w in edges:
    graph[u].append((v, w))

  heap = [(0, k)] # (starting weight, starting node)
  distances = {i: float('inf') for i in range(1, n + 1)} # all nodes set to infinity. adjust 1, n + 1 to whatever problem demands
  distances[k] = 0 # starting node distance is always 0

  while heap:
    current_distance, node = heapq.heappop(heap)
    if current_distance > distances[node]: # node was seen before and was pushed to the heap multiple times
      continue # also means this route was a candidate, but is now realized to be suboptimal
    
    for neighbor, weight in graph[node]:
      if current_distance + weight < distances[neighbor]: # a new candidate path
        distances[neighbor] = current_distance + weight
        heapq.heappush(heap, (current_distance + weight, neighbor))
    
  # finished
  # make sure to check for any infinities to see if any nodes weren't reached
  res = max(distances.values())
  return res if res != float('inf') else -1



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



