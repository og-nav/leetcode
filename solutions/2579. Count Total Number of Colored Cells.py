"""
Title: Count Total Number of Colored Cells
URL: https://leetcode.com/problems/count-total-number-of-colored-cells/description/
Difficulty: Medium
Tags: None
Topics: Math

Approach:
- derive formula to solve in O(1) time
- I used derivative to realize 2 coefficient in front of n ** 2
- bfs doesn't work because n is too big


Time Complexity: O(1)
Space Complexity: O(1)



Solution:
"""
from template import *

class Solution:
    def coloredCells(self, n: int) -> int:
        """
        1 -> 1
        2 -> 5 (1 + 4)
        3 -> 13 (5 + 8)
        4 -> 25 (13 + 12)

        2 * n ** 2 - 2 * n + 1
        """
        return 2 * n ** 2 - 2 * n + 1



"""
Question:

There exists an infinitely large two-dimensional grid of uncolored unit cells. You are given a positive integer n, indicating that you must do the following routine for n minutes:

At the first minute, color any arbitrary unit cell blue.
Every minute thereafter, color blue every uncolored cell that touches a blue cell.
Below is a pictorial representation of the state of the grid after minutes 1, 2, and 3.


Return the number of colored cells at the end of n minutes.

 

Example 1:

Input: n = 1
Output: 1
Explanation: After 1 minute, there is only 1 blue cell, so we return 1.
Example 2:

Input: n = 2
Output: 5
Explanation: After 2 minutes, there are 4 colored cells on the boundary and 1 in the center, so we return 5. 
 

Constraints:

1 <= n <= 105
"""