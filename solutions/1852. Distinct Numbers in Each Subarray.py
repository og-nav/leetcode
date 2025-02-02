"""
Title: Distinct Numbers in Each Subarray
URL: https://leetcode.com/problems/distinct-numbers-in-each-subarray/description/
Difficulty: Medium
Tags: Amazon
Topics: Array
Hash Table
Sliding Window


Approach:
- use a frequency counter + sliding window
- number of distinct numbers is just the length of the window

Time Complexity: O(n)
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        res = []
        counts = defaultdict(int)
        
        # initial counts
        for i in range(k):
            counts[nums[i]] += 1
        
        res.append(len(counts))
        for i in range(k, len(nums)):
            counts[nums[i]] += 1
            if counts[nums[i - k]] == 1:
                del counts[nums[i - k]]
            else:
                counts[nums[i - k]] -= 1
            
            res.append(len(counts))
        
        return res



"""
Question:

Given an integer array nums and an integer k, you are asked to construct the array ans of size n-k+1 where ans[i] is the number of distinct numbers in the subarray nums[i:i+k-1] = [nums[i], nums[i+1], ..., nums[i+k-1]].

Return the array ans.

 

Example 1:

Input: nums = [1,2,3,2,2,1,3], k = 3
Output: [3,2,2,2,3]
Explanation: The number of distinct elements in each subarray goes as follows:
- nums[0:2] = [1,2,3] so ans[0] = 3
- nums[1:3] = [2,3,2] so ans[1] = 2
- nums[2:4] = [3,2,2] so ans[2] = 2
- nums[3:5] = [2,2,1] so ans[3] = 2
- nums[4:6] = [2,1,3] so ans[4] = 3
Example 2:

Input: nums = [1,1,1,1,2,3,4], k = 4
Output: [1,2,3,4]
Explanation: The number of distinct elements in each subarray goes as follows:
- nums[0:3] = [1,1,1,1] so ans[0] = 1
- nums[1:4] = [1,1,1,2] so ans[1] = 2
- nums[2:5] = [1,1,2,3] so ans[2] = 3
- nums[3:6] = [1,2,3,4] so ans[3] = 4
 

Constraints:

1 <= k <= nums.length <= 105
1 <= nums[i] <= 105
"""