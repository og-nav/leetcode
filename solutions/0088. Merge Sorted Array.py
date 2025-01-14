"""
Title: Merge Sorted Array
URL: https://leetcode.com/problems/merge-sorted-array/
Difficulty: Easy
Tags: NeetCode 150, Grind, Meta

Approach:
- Naive: insert num2 into the end of nums1 and then sort
- Optimal: iterate backwards using 3 pointers
-- one pointer in for loop 
-- one pointer starting at the end of nums1
-- one pointer starting at the end of nums2
- p starts at m + n - 1, p1 starts at m - 1, p2 starts at n - 1
- if p2 is ever less than 0, we can just break since we know that the beginning of nums1 is already sorted
- then we can just make sure p1 is greater than 0 and if so, we check if nums1[p1] is greater than nums2[p2]
-- if so, we can place the value and decrement p1
- else, we place nums2's value and decrement p2
- some of nums1 values may ultimately be overwritten, but that's fine because they would have already been placed 
-- at the end of nums1 and are not needed anymore
- worst case is if all nums2 values are greater than all nums1 values -> no nums1 values will be overwritten


Time Complexity: O(m + n)
Space Complexity: O(1)



Solution:
"""
from template import *

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        p1 = m - 1
        p2 = n - 1

        for p in range(m + n - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1



"""
Question:

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
 

Follow up: Can you come up with an algorithm that runs in O(m + n) time?
"""