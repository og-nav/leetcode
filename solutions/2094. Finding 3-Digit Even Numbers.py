"""
Title: Finding 3-Digit Even Numbers
URL: https://leetcode.com/problems/finding-3-digit-even-numbers/description/
Difficulty: Easy
Tags: Meta, Google, Amazon
Topics: Array
Hash Table
Sorting
Enumeration

Approach:
- my first impulse was to brute force all the digits using backtracking
- but we can just realize that we only need to find 3 digit numbers
-- so we can just iterate from 100 to 999 and check all of them
--- this automatically knocks out the no leading 0 requirement
--- and we can step by two to knock out the even requirement
--- then we can just use a while loop to deconstruct all the digits
---- and then make sure that the number of a particualr digit doesn't exceed the amount in the digits array


Time Complexity: O(nlog(n)) -> n would be 100-999 and log(n) to deconstruct each digit. also the whole thing could be O(1) technically
Space Complexity: O(1) -> digits will only ever contain 1-9



Solution:
"""
from template import *

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        count = defaultdict(int)
        for d in digits:
            count[d] += 1
        
        res = []
        for i in range(100, 999, 2):
            nums = defaultdict(int)
            n = i
            while n >= 1:
                nums[n % 10] += 1
                n //= 10
            
            for digit in nums:
                if nums[digit] > count[digit]:
                    break
            else:
                res.append(i)
        
        return res



"""
Question:

You are given an integer array digits, where each element is a digit. The array may contain duplicates.

You need to find all the unique integers that follow the given requirements:

The integer consists of the concatenation of three elements from digits in any arbitrary order.
The integer does not have leading zeros.
The integer is even.
For example, if the given digits were [1, 2, 3], integers 132 and 312 follow the requirements.

Return a sorted array of the unique integers.

 

Example 1:

Input: digits = [2,1,3,0]
Output: [102,120,130,132,210,230,302,310,312,320]
Explanation: All the possible integers that follow the requirements are in the output array. 
Notice that there are no odd integers or integers with leading zeros.
Example 2:

Input: digits = [2,2,8,8,2]
Output: [222,228,282,288,822,828,882]
Explanation: The same digit can be used as many times as it appears in digits. 
In this example, the digit 8 is used twice each time in 288, 828, and 882. 
Example 3:

Input: digits = [3,7,5]
Output: []
Explanation: No even integers can be formed using the given digits.
 

Constraints:

3 <= digits.length <= 100
0 <= digits[i] <= 9
"""