"""
Title: Kth Largest Element in an Array
URL: https://leetcode.com/problems/kth-largest-element-in-an-array/description/
Difficulty: Medium
Tags: NeetCode 150, Grind, Meta, Amazon, Google, Microsoft, Adobe, Yahoo, Uber, Salesforce

Approach:
- create a minHeap
- iterate through nums and push to heap
- if length of minHeap is greater than k, we can just pop
- Meta might ask to solve using quick select for O(n) TC


Time Complexity: O(nlog(k)) -> n elements and we perform a log(k) move per element (popping the heap)
Space Complexity: O(k) -> heap only ever holds k elements at a time



Solution:
"""
from template import *

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for n in nums:
            heapq.heappush(minHeap, n)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        return minHeap[0]



"""
Question:

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
"""