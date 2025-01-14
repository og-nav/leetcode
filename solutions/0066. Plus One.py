"""
Title: Plus One
URL: https://leetcode.com/problems/plus-one/description/
Difficulty: Easy
Tags: NeetCode 150, Meta, Google, Amazon, Bloomberg, Microsoft, Adobe, Apple, Yahoo, Uber
Topics: Array
Math


Approach:
- just need to check a few edge cases
- like if last digit isn't 9 we just increment it and return
- then reverse the array and iterate and any 9s become 0
-- once you don't find a 9, just increment and return
- lastly, if the entire array is all 9s (go through entire for loop), just append a 1, reverse, and return
- carry variable isn't needed


Time Complexity: O(n)
Space Complexity: O(n) (could be O(1) if you modify the input array instead of making a copy)



Solution:
"""
from template import *

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        
        digits = digits[::-1]
        for i in range(len(digits)):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits[::-1]

        digits.append(1)
        return digits[::-1]



"""
Question:

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
 

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.
"""