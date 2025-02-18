"""
Title: Calculate Money in Leetcode Bank
URL: https://leetcode.com/problems/calculate-money-in-leetcode-bank/description/
Difficulty: Easy
Tags: Google, Amazon
Topics: Math

Approach:
- can just simulate
- deceptively tricky
- there's also an O(1) math solution


Time Complexity: O(n)
Space Complexity: O(1)



Solution:
"""
from template import *

class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0
        monday = 1
        deposit = 0
        for i in range(n):
            if i % 7 == 0:
                res += monday
                monday += 1
                deposit = monday
            else:
                res += deposit
                deposit += 1
        
        return res



"""
Question:

Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.

Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

 

Example 1:

Input: n = 4
Output: 10
Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.
Example 2:

Input: n = 10
Output: 37
Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2nd Monday, Hercy only puts in $2.
Example 3:

Input: n = 20
Output: 96
Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.
 

Constraints:

1 <= n <= 1000
"""