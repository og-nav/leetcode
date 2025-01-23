"""
Title: Path Crossing
URL: https://leetcode.com/problems/path-crossing/description/
Difficulty: Easy
Tags: Amazon, Google, Microsoft
Topics: Hash Table
String

Approach:
- just use x, y coordinates and increment/decrement depending on direction
- keep visited set


Time Complexity: O(n)
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visit = set([(0, 0)])
        x, y = 0, 0
        for p in path:
            if p == "N":
                x += 1
            elif p == "S":
                x -= 1
            elif p == "E":
                y += 1
            else:
                y -= 1
            
            if (x, y) in visit:
                return True
            
            visit.add((x, y))
        
        return False



"""
Question:

Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.

 

Example 1:


Input: path = "NES"
Output: false 
Explanation: Notice that the path doesn't cross any point more than once.
Example 2:


Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.
 

Constraints:

1 <= path.length <= 104
path[i] is either 'N', 'S', 'E', or 'W'.
"""