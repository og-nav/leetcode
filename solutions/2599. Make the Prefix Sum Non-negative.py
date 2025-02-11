"""
Title: Make the Prefix Sum Non-negative
URL: https://leetcode.com/problems/make-the-prefix-sum-non-negative/description/
Difficulty: Medium
Tags: Microsoft
Topics: Array
Greedy
Heap (Priority Queue)

Approach:
- need to realize we need the number of operations and don't really need to keep track of the actual prefix sum
- and that being too greedy and moving the number that immediately makes the running total negative is 
-- not always the optimal
- the optimal is to "move" the smallest number encountered to the end
- so we can use a min heap
- since we don't need to return the final array, we can consider the pop to be the operation and just increment


Time Complexity: O(nlog(n))
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        heap = []
        running_total = 0
        res = 0

        for n in nums:
            if running_total < 0:
                smallest = heapq.heappop(heap)
                running_total -= smallest
                res += 1
            
            heapq.heappush(heap, n)
            running_total += n
        
        return res



"""
Question:

You are given a 0-indexed integer array nums. You can apply the following operation any number of times:

Pick any element from nums and put it at the end of nums.
The prefix sum array of nums is an array prefix of the same length as nums such that prefix[i] is the sum of all the integers nums[j] where j is in the inclusive range [0, i].

Return the minimum number of operations such that the prefix sum array does not contain negative integers. The test cases are generated such that it is always possible to make the prefix sum array non-negative.

 

Example 1:

Input: nums = [2,3,-5,4]
Output: 0
Explanation: we do not need to do any operations.
The array is [2,3,-5,4]. The prefix sum array is [2, 5, 0, 4].
Example 2:

Input: nums = [3,-5,-2,6]
Output: 1
Explanation: we can do one operation on index 1.
The array after the operation is [3,-2,6,-5]. The prefix sum array is [3, 1, 7, 2].
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""