"""
Title: Palindrome Number
URL: https://leetcode.com/problems/palindrome-number/description/
Difficulty: Easy
Tags: Grind, Google, Meta, Microsoft, Amazon, Bloomberg, Apple, Adobe
Topics: Math

Approach:
- just need to make a reverse integer to keep track and do some mod work
- also avoid test cases like < 0 and any number ending in 0 that isn't 0, etc


Time Complexity: O(log(n)) -> since we divide by 10 each time
Space Complexity: O(1)



Solution:
"""
from template import *

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or x > 0 and x % 10 == 0:
            return False
        
        copy = x
        reverse = 0
        while x:
            digit = x % 10
            reverse = reverse * 10 + digit
            x //= 10
 
        return reverse == copy



"""
Question:

Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
"""