"""
Title: Strobogrammatic Number
URL: https://leetcode.com/problems/strobogrammatic-number/description/
Difficulty: Easy
Tags: Meta, Google, Uber
Topics: Hash Table
Two Pointers
String

Approach:
- just need to keep a set of numbers that don't look normal when turned upside down
- then it's just two pointer with a bunch of ifs


Time Complexity: O(n)
Space Complexity: O(1)



Solution:
"""
from template import *

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        invalid = "23457"
        l, r = 0, len(num) - 1
        while l <= r:
            if num[l] in invalid or num[r] in invalid:
                return False
            
            if num[l] == '0':
                if num[r] != '0':
                    return False
            elif num[l] == '1':
                if num[r] != '1':
                    return False
            elif num[l] == '6':
                if num[r] != '9':
                    return False
            elif num[l] == '8':
                if num[r] != '8':
                    return False
            elif num[l] == '9':
                if num[r] != '6':
                    return False
            
            l += 1
            r -= 1

        return True
            



"""
Question:

Given a string num which represents an integer, return true if num is a strobogrammatic number.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

 

Example 1:

Input: num = "69"
Output: true
Example 2:

Input: num = "88"
Output: true
Example 3:

Input: num = "962"
Output: false
 

Constraints:

1 <= num.length <= 50
num consists of only digits.
num does not contain any leading zeros except for zero itself.
"""