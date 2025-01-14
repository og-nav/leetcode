"""
Title: K Empty Slots
URL: https://leetcode.com/problems/k-empty-slots/description/
Difficulty: Hard
Tags: Google
Topics: Array
Binary Indexed Tree
Segment Tree
Queue
Sliding Window
Heap (Priority Queue)
Ordered Set
Monotonic Queue

Approach:
- there are a few ways to solve in O(n) using heap, monotonic queue, and sliding window, but based on my skill level,
-- brute force solution is the way to go 
- basically keep a state array and each time you add a bulb, iterate k spots left and right and make sure none
-- are already turned on
- then check one more space to make sure it's on
- I also modified bulbs array to make it 0-indexed


Time Complexity: O(n * k)
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        if k > len(bulbs):
            return -1
        
        state = [0] * len(bulbs)
        bulbs = [x - 1 for x in bulbs]

        for i, b in enumerate(bulbs):
            # turn on this bulb
            state[b] = 1

            # check left
            for j in range(k):
                if b - 1 - j < 0 or state[b - 1 - j] == 1:
                    break
            else:
                if b - 1 - k >= 0 and state[b - 1 - k] == 1:
                    return i + 1

            # check right
            for j in range(k):
                if b + 1 + j >= len(state) or state[b + 1 + j] == 1:
                    break
            else:
                if b + 1 + k < len(state) and state[b + 1 + k] == 1:
                    return i + 1
        
        return -1



"""
Question:

You have n bulbs in a row numbered from 1 to n. Initially, all the bulbs are turned off. We turn on exactly one bulb every day until all bulbs are on after n days.

You are given an array bulbs of length n where bulbs[i] = x means that on the (i+1)th day, we will turn on the bulb at position x where i is 0-indexed and x is 1-indexed.

Given an integer k, return the minimum day number such that there exists two turned on bulbs that have exactly k bulbs between them that are all turned off. If there isn't such day, return -1.

 

Example 1:

Input: bulbs = [1,3,2], k = 1
Output: 2
Explanation:
On the first day: bulbs[0] = 1, first bulb is turned on: [1,0,0]
On the second day: bulbs[1] = 3, third bulb is turned on: [1,0,1]
On the third day: bulbs[2] = 2, second bulb is turned on: [1,1,1]
We return 2 because on the second day, there were two on bulbs with one off bulb between them.
Example 2:

Input: bulbs = [1,2,3], k = 1
Output: -1
 

Constraints:

n == bulbs.length
1 <= n <= 2 * 104
1 <= bulbs[i] <= n
bulbs is a permutation of numbers from 1 to n.
0 <= k <= 2 * 104

"""