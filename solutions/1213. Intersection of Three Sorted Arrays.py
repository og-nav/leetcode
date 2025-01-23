"""
Title: Intersection of Three Sorted Arrays
URL: https://leetcode.com/problems/intersection-of-three-sorted-arrays/description/
Difficulty: Easy
Tags: Meta
Topics: Array
Hash Table
Binary Search
Counting

Approach:
- use 3 pointers
- leverage the fact that arrays are sorted
- from an interview perspective, discuss with interviewer what would happen if one array was very small
-- and the other two are very big; avoid urge to jump in and code with assumption that all arrays are the same size
- if this is the case, we are better off using binary search to find if the values in the small array exist
-- in the bigger arrays


Time Complexity: O(n)
Space Complexity: O(1) -> result array does not count towards space complexity



Solution:
"""
from template import *

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        res = []
        i, j, k = 0, 0, 0

        while i < len(arr1) and j < len(arr2) and k < len(arr3):
            if arr1[i] == arr2[j] and arr2[j] == arr3[k]:
                res.append(arr1[i])
                i += 1
                j += 1
                k += 1
            else:
                if arr1[i] < arr2[j]:
                    i += 1
                elif arr2[j] < arr3[k]:
                    j += 1
                else:
                    k += 1
        
        return res



"""
Question:

Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.

 

Example 1:

Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
Output: [1,5]
Explanation: Only 1 and 5 appeared in the three arrays.
Example 2:

Input: arr1 = [197,418,523,876,1356], arr2 = [501,880,1593,1710,1870], arr3 = [521,682,1337,1395,1764]
Output: []
 

Constraints:

1 <= arr1.length, arr2.length, arr3.length <= 1000
1 <= arr1[i], arr2[i], arr3[i] <= 2000
"""