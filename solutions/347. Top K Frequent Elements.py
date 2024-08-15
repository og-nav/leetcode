"""
Title: Top K Frequent Elements
URL: https://leetcode.com/problems/top-k-frequent-elements/description/
Difficulty: Medium

Approach:
- populate dictionary with counts of all numbers in n
- initialize minHeap
- we want to push (d[key], key) tuples to heap
- if len(minHeap) > k: we pop the minheap
- lastly, we iterate through the heap and append values to the result array


Time Complexity: O(nlog(k)) 
--- O(klog(k) + (n - k)log(k) = nlog(k))
Space Complexity: O(n + k)
-- O(n) for hashmap, O(k) for heap with k elements


Solution:
"""
from template import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        
        minHeap = []
        heapq.heapify(minHeap)

        for key in d:
            heapq.heappush(minHeap, (d[key], key))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        res = []
        for _, num in minHeap:
            res.append(num)
        
        return res



"""
Question:

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
"""