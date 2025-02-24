"""
Title: Numbers With Same Consecutive Differences
URL: https://leetcode.com/problems/numbers-with-same-consecutive-differences/description/
Difficulty: Medium
Tags: None
Topics: Backtracking
Breadth-First Search

Approach:
- brute force backtrack or bfs


Time Complexity: O(2 ^ n)
Space Complexity: O(2 ^ n)



Solution:
"""
from template import *

class Solution:
    # bfs
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = set()
        queue = deque([str(x) for x in range(1, 10)])
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                
                if len(curr) == n:
                    res.add(int(curr))
                    continue
                
                for neighbor in [int(curr[-1]) + k, int(curr[-1]) - k]:
                    if neighbor >= 0 and neighbor < 10:
                        queue.append(curr + str(neighbor))
        
        return list(res)

class Solution:
    # backtracking
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []
    
        def backtrack(curr):
            if len(curr) == n:
                res.append(int(curr))
                return
            
            for i in range(0, 10):
                if abs(int(curr[-1]) - i) == k:
                    backtrack(curr + str(i))


        for i in range(1, 10):
            backtrack(str(i))
        
        return res


"""
Question:

Given two integers n and k, return an array of all the integers of length n where the difference between every two consecutive digits is k. You may return the answer in any order.

Note that the integers should not have leading zeros. Integers as 02 and 043 are not allowed.

 

Example 1:

Input: n = 3, k = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
Example 2:

Input: n = 2, k = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
 

Constraints:

2 <= n <= 9
0 <= k <= 9
"""