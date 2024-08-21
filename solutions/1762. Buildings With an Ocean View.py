"""
Title: Buildings with an Ocean View
URL: https://leetcode.com/problems/buildings-with-an-ocean-view/description/
Difficulty: Medium
Tags: NeetCode 150, Grind, Meta

Approach:
- just iterate right to left, keeping track of the highest building occured so far (initialize to 0)
- if current building's height is greater than highest, append index to res array then set highest to new height
- return reversed array


Time Complexity: O(n)
Space Complexity: O(1) -> return array not counted in space complexity, would be O(n) if so. also reverse can be done
        in place in O(n) time so Time Complexity is still O(n).



Solution:
"""
from template import *

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        highest = 0
        res = []
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > highest:
                res.append(i)
                highest = heights[i]
        
        return res[::-1]



"""
Question:

There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.

The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height.

Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

 

Example 1:

Input: heights = [4,2,3,1]
Output: [0,2,3]
Explanation: Building 1 (0-indexed) does not have an ocean view because building 2 is taller.
Example 2:

Input: heights = [4,3,2,1]
Output: [0,1,2,3]
Explanation: All the buildings have an ocean view.
Example 3:

Input: heights = [1,3,2,4]
Output: [3]
Explanation: Only building 3 has an ocean view.
 

Constraints:

1 <= heights.length <= 105
1 <= heights[i] <= 109
"""