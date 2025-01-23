"""
Title: Intersection of Multiple Arrays
URL: https://leetcode.com/problems/intersection-of-multiple-arrays/description/
Difficulty: Easy
Tags: Uber, Meta, Amazon
Topics: Array
Hash Table
Sorting
Counting

Approach:
- leverage the fact that all numbers in each row of nums are unique
- so a number that appears in all arrays will have a frequency of len(nums) in a frequency counter
- one trick to watch out for:
-- not all subarrays are the same size
-- so when iterating using double for loop, make sure j goes in range of len(nums[i]) rather than autopiloting nums[0]
- lastly, if numbers were not unique, we could just convert each row to a set and do intersection

Time Complexity: O(m * n)
Space Complexity: O(m * n)


Solution:
"""
from template import *

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        counts = defaultdict(int)
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                counts[nums[i][j]] += 1
        
        res = []
        for n in counts:
            if counts[n] == len(nums):
                res.append(n)
        
        return sorted(res)



"""
Question:

Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return the list of integers that are present in each array of nums sorted in ascending order.
 

Example 1:

Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
Output: [3,4]
Explanation: 
The only integers present in each of nums[0] = [3,1,2,4,5], nums[1] = [1,2,3,4], and nums[2] = [3,4,5,6] are 3 and 4, so we return [3,4].
Example 2:

Input: nums = [[1,2,3],[4,5,6]]
Output: []
Explanation: 
There does not exist any integer present both in nums[0] and nums[1], so we return an empty list [].
 

Constraints:

1 <= nums.length <= 1000
1 <= sum(nums[i].length) <= 1000
1 <= nums[i][j] <= 1000
All the values of nums[i] are unique.
"""