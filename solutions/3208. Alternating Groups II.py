"""
Title: Alternating Groups II
URL: https://leetcode.com/problems/alternating-groups-ii/description/
Difficulty: Medium
Tags: Google
Topics: Array
Sliding Window

Approach:
- pseudo-sliding window where we just keep track of a running length of valid sequence
- note that the actual colors don't matter
- we just reset the running count whenever we encounter doubles
- and we use mod operations to capture the wrap-arounds


Time Complexity: O(n + k)
Space Complexity: O(1)



Solution:
"""
from template import *

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        res = 0
        current_group_length = 1
        for i in range(1, len(colors) + k - 1):
            # add the new element to the window
            current_group_length += 1

            # calculate new index using mod so we wrap around
            index = i % len(colors)

            # reset group if current color matches previous color
            if colors[index] == colors[index - 1]:
                current_group_length = 1
            
            # add to result if current_group_length is >= k
            # we know that each number greater than k means one more valid sequence
            # since "left pointer" would have implicitly moved up
            if current_group_length >= k:
                res += 1
            
        return res



"""
Question:

There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile i is represented by colors[i]:

colors[i] == 0 means that tile i is red.
colors[i] == 1 means that tile i is blue.
An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except the first and last one has a different color from its left and right tiles).

Return the number of alternating groups.

Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.

 

Example 1:

Input: colors = [0,1,0,1,0], k = 3

Output: 3

Explanation:



Alternating groups:



Example 2:

Input: colors = [0,1,0,0,1,0,1], k = 6

Output: 2

Explanation:



Alternating groups:



Example 3:

Input: colors = [1,1,0,1], k = 4

Output: 0

Explanation:



 

Constraints:

3 <= colors.length <= 105
0 <= colors[i] <= 1
3 <= k <= colors.length
"""