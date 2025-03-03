"""
Title: Most Profitable Path in a Tree
URL: https://leetcode.com/problems/most-profitable-path-in-a-tree/description/
Difficulty: Medium
Tags: Snowflake, Meta, Amazon, Google
Topics: Array
Tree
Depth-First Search
Breadth-First Search
Graph

Approach:
- problem is not that hard once you understand, but requires some key insights
-- since graph is a tree, Bob only has one path to the root
-- a leaf node in an undirected graph is just a node whose only neighbor is its parent
- we can first calculate bob's movement independently
-- use dfs w/ backtracking to calculate the path because we need to save the path
--- doing bfs will end up in O(n ^ 2) time complexity since we need to keep rebuilding the path to put it in queue
- then we can do bfs from Alice to the leaf nodes
- we need to use a time variable in between each bfs step to calculate bob's movement
- then we can just follow rules accordingly 


Time Complexity: O(n)
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # calculate bob path to root (only 1)
        bob_path = []
        visit = set()
        def dfs(node, path):
            nonlocal bob_path
            if node in visit:
                return
            if node == 0:
                bob_path = path[::]
                bob_path.append(0)
                return
            
            visit.add(node)
            path.append(node)
            for neighbor in graph[node]:
                dfs(neighbor, path)
            path.pop()
        
        dfs(bob, [])

        # calculate all Alice paths to leaf nodes
        # while calculating these paths, reference bob's movement and calculate profit accordingly
        res = float('-inf')
        time = -1
        opened = set() # gates that bob has opened
        visit = set([0])
        queue = deque([(0, 0, 0)]) # current node, current profit, previous node
        while queue:
            time += 1
            if time < len(bob_path):
                opened.add(bob_path[time])

            for _ in range(len(queue)):
                node, profit, prev = queue.popleft()
                
                # reached at the same time
                if time < len(bob_path) and bob_path[time] == node:
                    profit += amount[node] // 2
                
                # alice reached the gate first
                elif node not in opened:
                    profit += amount[node]

                # check if we are on a leaf node
                if graph[node] == [prev]:
                    res = max(res, profit)
                    
                for neighbor in graph[node]:
                    if neighbor not in visit:
                        visit.add(neighbor)
                        queue.append((neighbor, profit, node))
        
        return res



"""
Question:

There is an undirected tree with n nodes labeled from 0 to n - 1, rooted at node 0. You are given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

At every node i, there is a gate. You are also given an array of even integers amount, where amount[i] represents:

the price needed to open the gate at node i, if amount[i] is negative, or,
the cash reward obtained on opening the gate at node i, otherwise.
The game goes on as follows:

Initially, Alice is at node 0 and Bob is at node bob.
At every second, Alice and Bob each move to an adjacent node. Alice moves towards some leaf node, while Bob moves towards node 0.
For every node along their path, Alice and Bob either spend money to open the gate at that node, or accept the reward. Note that:
If the gate is already open, no price will be required, nor will there be any cash reward.
If Alice and Bob reach the node simultaneously, they share the price/reward for opening the gate there. In other words, if the price to open the gate is c, then both Alice and Bob pay c / 2 each. Similarly, if the reward at the gate is c, both of them receive c / 2 each.
If Alice reaches a leaf node, she stops moving. Similarly, if Bob reaches node 0, he stops moving. Note that these events are independent of each other.
Return the maximum net income Alice can have if she travels towards the optimal leaf node.

 

Example 1:


Input: edges = [[0,1],[1,2],[1,3],[3,4]], bob = 3, amount = [-2,4,2,-4,6]
Output: 6
Explanation: 
The above diagram represents the given tree. The game goes as follows:
- Alice is initially on node 0, Bob on node 3. They open the gates of their respective nodes.
  Alice's net income is now -2.
- Both Alice and Bob move to node 1. 
  Since they reach here simultaneously, they open the gate together and share the reward.
  Alice's net income becomes -2 + (4 / 2) = 0.
- Alice moves on to node 3. Since Bob already opened its gate, Alice's income remains unchanged.
  Bob moves on to node 0, and stops moving.
- Alice moves on to node 4 and opens the gate there. Her net income becomes 0 + 6 = 6.
Now, neither Alice nor Bob can make any further moves, and the game ends.
It is not possible for Alice to get a higher net income.
Example 2:


Input: edges = [[0,1]], bob = 1, amount = [-7280,2350]
Output: -7280
Explanation: 
Alice follows the path 0->1 whereas Bob follows the path 1->0.
Thus, Alice opens the gate at node 0 only. Hence, her net income is -7280. 
 

Constraints:

2 <= n <= 105
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
ai != bi
edges represents a valid tree.
1 <= bob < n
amount.length == n
amount[i] is an even integer in the range [-104, 104].
"""