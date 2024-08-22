"""
Title: K Closest Points to Origin
URL: https://leetcode.com/problems/k-closest-points-to-origin/description/
Difficulty: Medium
Tags: NeetCode 150, Grind, Meta

Approach:
- main idea is to store elements in a max heap
- which means distance needs to be put in as a negative
- this way, heap will only contain smallest numbers
- iterate through points, calculate distance, push (-distance, [x, y]) to maxHeap
- if len(maxHeap) > k, pop the heap
- lastly, use list comprehension to build result


Time Complexity: O(nlog(k)) -> we perform a log(k) function (popping the heap) for each element
Space Complexity: O(k) -> only k elements are stored in heap at a time



Solution:
"""
from template import *

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        
        for x, y in points:
            distance = sqrt(x ** 2 + y ** 2)
            heapq.heappush(maxHeap, (-distance, [x, y]))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        return [p[1] for p in maxHeap]



"""
Question:

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

 

Example 1:


Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
 

Constraints:

1 <= k <= points.length <= 104
-104 <= xi, yi <= 104
"""