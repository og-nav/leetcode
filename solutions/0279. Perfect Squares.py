"""
Title: Perfect Squares
URL: https://leetcode.com/problems/perfect-squares/description/
Difficulty: Medium
Tags: Google, Microsoft, Amazon, Apple, Bloomberg, Meta
Topics: Math
Dynamic Programming
Breadth-First Search

Approach:
- I solved by generating all squares and then using bfs (visualized as a n-ary tree)
- need a visit set or else MLE
- can also be solved the exact same way as coin change via dynamic programming


Time Complexity: O(sqrt(n) ^ h) -> in both cases, we create children of size sqrt(n) (gained from finding all squares) for each node. so go until result is reached (ultimately the height of the tree).
Space Complexity: O(sqrt(n) ^ h)



Solution:
"""
from template import *

class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        for i in range(1, int(n ** 0.5) + 1):
            squares.append(i ** 2)
        
        count = -1
        visit = set([0])
        queue = deque([0])
        while queue:
            count += 1
            for _ in range(len(queue)):
                total = queue.popleft()

                if total == n:
                    return count
                elif total > n:
                    continue
                
                for square in squares:
                    new_total = total + square
                    if new_total not in visit:
                        visit.add(new_total)
                        queue.append(new_total)
        
        return -1



"""
Question:

Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

 

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
 

Constraints:

1 <= n <= 104
"""