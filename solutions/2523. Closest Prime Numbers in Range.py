"""
Title: Closest Prime Numbers in Range
URL: https://leetcode.com/problems/closest-prime-numbers-in-range/
Difficulty: Medium
Tags: TikTok
Topics: Math
Number Theory

Approach:
- question will most likely not be asked in interview
- use a helper is_prime function and evaluate only 2 adjacent primes at a time
- can return if the difference is less than or equal to 2 due to some twin primes theorem


Time Complexity: O(min(1452, R - L) * sqrt(R))
Space Complexity: O(1)



Solution:
"""
from template import *

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def is_prime(n):
            if n == 1:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            
            return True

        a = -1
        b = -1
        difference = right - left + 1
        res = [a, b]
        for i in range(left, right + 1):
            if is_prime(i):
                a = b
                b = i
            
            if a > 0 and b > 0:
                current_difference = b - a
                if current_difference <= 2:
                    return [a, b]
                elif current_difference < difference:
                    difference = current_difference
                    res[0] = a
                    res[1] = b
        
        return res



"""
Question:

Given two positive integers left and right, find the two integers num1 and num2 such that:

left <= num1 < num2 <= right .
Both num1 and num2 are prime numbers.
num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].

 

Example 1:

Input: left = 10, right = 19
Output: [11,13]
Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.
Example 2:

Input: left = 4, right = 6
Output: [-1,-1]
Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.
 

Constraints:

1 <= left <= right <= 106
"""