"""
Title: Jump Game III
URL: https://leetcode.com/problems/jump-game-iii/description/
Difficulty: Medium
Tags: Pinterest, Microsoft

Approach:
- stock 2d bfs but just with 1d array
- need to modify invalid function a little bit but p much the same as usual 
- where we need to validate i + arr[i] square before appending to queue


Time Complexity: O(n)
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def invalid(i):
            return i < 0 or i >= len(arr)
        
        if arr[start] == 0:
            return True
        
        queue = deque([start])
        visit = set([start])
        while queue:
            for _ in range(len(queue)):
                i = queue.popleft()
                if arr[i] == 0:
                    return True
                
                if not invalid(i + arr[i]) and i + arr[i] not in visit:
                    queue.append(i + arr[i])
                    visit.add(i + arr[i])
                if not invalid(i - arr[i]) and i - arr[i] not in visit:
                    queue.append(i - arr[i])
                    visit.add(i - arr[i])
        
        return False




"""
Question:

Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach any index with value 0.

Notice that you can not jump outside of the array at any time.

 

Example 1:

Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation: 
All possible ways to reach at index 3 with value 0 are: 
index 5 -> index 4 -> index 1 -> index 3 
index 5 -> index 6 -> index 4 -> index 1 -> index 3 
Example 2:

Input: arr = [4,2,3,0,3,1,2], start = 0
Output: true 
Explanation: 
One possible way to reach at index 3 with value 0 is: 
index 0 -> index 4 -> index 1 -> index 3
Example 3:

Input: arr = [3,0,2,1,2], start = 2
Output: false
Explanation: There is no way to reach at index 1 with value 0.
 

Constraints:

1 <= arr.length <= 5 * 104
0 <= arr[i] < arr.length
0 <= start < arr.length
"""