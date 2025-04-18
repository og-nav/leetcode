"""
Title: Count and Say 
URL: https://leetcode.com/problems/count-and-say/description/
Difficulty: Medium
Tags: Google, Meta, Microsoft, Amazon, Pinterest, APple, Bloomberg
Topics: String

Approach:
- create a helper function that can create run length encoding of any string
- then brute force


Time Complexity: O(4 ^ (n / 3))
Space Complexity: O(4 ^ (n / 3))

- apparently, every 3 recursions, the length increases by a power of 4 at the upper bound



Solution:
"""
from template import *

class Solution:
    def countAndSay(self, n: int) -> str:
        def rle(s):       
            res = []
            i = 0 
            while i < len(s):
                n = s[i]
                count = 0
                while i < len(s) and s[i] == n:
                    count += 1
                    i += 1
                
                res.append(str(count))
                res.append(n)

            return "".join(res)
        
        res = "1"
        for _ in range(n - 1):
            res = rle(res)
        
        return res



"""
Question:

The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the run-length encoding of countAndSay(n - 1).
Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15" and replace "1" with "11". Thus the compressed string becomes "23321511".

Given a positive integer n, return the nth element of the count-and-say sequence.

 

Example 1:

Input: n = 4

Output: "1211"

Explanation:

countAndSay(1) = "1"
countAndSay(2) = RLE of "1" = "11"
countAndSay(3) = RLE of "11" = "21"
countAndSay(4) = RLE of "21" = "1211"
Example 2:

Input: n = 1

Output: "1"

Explanation:

This is the base case.

 

Constraints:

1 <= n <= 30
 

Follow up: Could you solve it iteratively?
"""