from collections import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
LOOP
'''
# break out of nested for loop
for i in range(10):
    for j in range(10):
        # something
        if True: # if break condition is true
            break
    else:
        continue
    break

'''
GRAPH
'''
# create undirected graph from binary tree
graph = defaultdict(list)
def dfs(node):
    if node is None:
        return
    if node.left:
        graph[node.val].append(node.left.val)
        graph[node.left.val].append(node.val)
    if node.right:
        graph[node.val].append(node.right.val)
        graph[node.right.val].append(node.val)

    dfs(node.left)
    dfs(node.right)

# create undirected graph from list of edges
def edges_to_graph(edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)


'''
SORT
'''
# sort by first element in tuple
## defaults to second item if tied
### this avoids it in cases you don't want that
#### (i.e. vertical order traversal)
column = [(2, 11), (2, 10), (1, 9)]
column.sort(key=lambda x: x[0])