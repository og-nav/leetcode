"""
Title: Divide Array Into Equal Pairs
URL: https://leetcode.com/problems/divide-array-into-equal-pairs/description/
Difficulty: Easy
Tags: Microsoft
Topics: Array
Hash Table
Bit Manipulation
Counting

Approach:
- need to realize that all numbers must occur in an even amount
- so just add to set and remove if encountered a second time
- and any elements in set means impossible


Time Complexity: O(n)
Space Complexity: O(n) -> in worst case all elements are unique



Solution:
"""
from template import *

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        visit = set()

        for n in nums:
            if n in visit:
                visit.remove(n)
            else:
                visit.add(n)
        
        return len(visit) == 0



"""
Question:

You are given an integer array nums consisting of 2 * n integers.

You need to divide nums into n pairs such that:

Each element belongs to exactly one pair.
The elements present in a pair are equal.
Return true if nums can be divided into n pairs, otherwise return false.

 

Example 1:

Input: nums = [3,2,3,2,2,2]
Output: true
Explanation: 
There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.
Example 2:

Input: nums = [1,2,3,4]
Output: false
Explanation: 
There is no way to divide nums into 4 / 2 = 2 pairs such that the pairs satisfy every condition.
 

Constraints:

nums.length == 2 * n
1 <= n <= 500
1 <= nums[i] <= 500
"""