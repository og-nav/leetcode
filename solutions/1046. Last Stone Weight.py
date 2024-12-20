"""
Title: Last Stone Weight
URL: https://leetcode.com/problems/last-stone-weight/description/
Difficulty: Easy
Tags: NeetCode 150
Topics: Array
Heap (Priority Queue)

Approach:
- use max heap (negate values to simulate it)
- while length max heap > 1, pop two elements, and if they aren't equal, push to the heap
- remember to use max heap here because when we pop, we want the biggest element
- unlike min heaps which pop the smallest element


Time Complexity: O(nlog(n)) # heapify is O(n) but tc comes from a log(n) operation occuring for n elements in the array.
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)
            
            if a != b:
                heapq.heappush(heap, -abs(a - b))
        
        if len(heap) == 1:
            return -heap[0]
        return 0



"""
Question:

You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.

 

Example 1:

Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
Example 2:

Input: stones = [1]
Output: 1
 

Constraints:

1 <= stones.length <= 30
1 <= stones[i] <= 1000
"""