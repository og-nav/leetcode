"""
Title: Relative Sort Array
URL: https://leetcode.com/problems/relative-sort-array/description/
Difficulty: Easy
Tags: Amazon, Meta, Google, Bloomberg, Adobe
Topics: Array
Hash Table
Sorting
Counting Sort

Approach:
- create counter for arr1, then iterate thru arr2 and append to res for _ in range(counts[n])
- then delete the dictionary element using del counts[n]
- then just create an extras array
-- make sure to also do for _ in range(counts[key]) again cuz I forgot both times I solved this problem over a year apart
- also there's a cheese method to reduce time complexity even further by utilizing low constraints
- instead of sorting extra at the end, we just find the max value of the array originally and use a for loop up to it
- that way it gets added in order


Time Complexity: O(m + nlog(n)) -> m time for arr1 counter, then nlogn to sort extra
Space Complexity: O(m + n) -> m space for arr1 counter, then n to sort extra since Python uses Timsort



Solution:
"""
from template import *

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        counts = defaultdict(int)
        for n in arr1:
            counts[n] += 1
        
        for n in arr2:
            for _ in range(counts[n]):
                res.append(n)
            del counts[n]
        
        extra = []
        for key in counts:
            for _ in range(counts[key]):
                extra.append(key)
        
        extra.sort()
        return res + extra



"""
Question:

Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

 

Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
Example 2:

Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
Output: [22,28,8,6,17,44]
 

Constraints:

1 <= arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
All the elements of arr2 are distinct.
Each arr2[i] is in arr1.
"""