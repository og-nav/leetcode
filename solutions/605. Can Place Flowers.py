"""
Title: Can Place Flowers
URL: https://leetcode.com/problems/can-place-flowers/description/
Difficulty: Easy
Tags: LinkedIn, Meta, Google, Microsoft, Amazon, Bloomberg, Apple
Topics: Array
Greedy

Approach:
- very deceptively tricky problem with lots of edge cases
- should be practiced once before interview
- but basically want to place flowers greedily whenever possible
- need to be aware of edge case where array ends in [1, 0, 0] so need to check to make sure if 0 is last element of array
-- got this wrong my first try

Time Complexity: O(n)
Space Complexity: O(1)



Solution:
"""
from template import *

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 1:
                i += 2
            else:
                if i == len(flowerbed) - 1 or i < len(flowerbed) - 1 and flowerbed[i + 1] == 0:
                    n -= 1
                    i += 2
                else:
                    i += 3
        
        return n <= 0



"""
Question:

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""