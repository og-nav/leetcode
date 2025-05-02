"""
Title: Largest Time for Given Digits
URL: https://leetcode.com/problems/largest-time-for-given-digits/description/
Difficulty: Medium
Tags: Microsoft, Google, Amazon
Topics: Array
String
Backtracking
Enumeration

Approach:
- brute force permutation by backtracking
- just sort nums in reverse at the beginning 
-- so that the first valid time found is the answer


Time Complexity: O(1) -> since there are only 4 otherwise n! if variable length
Space Complexity: O(1)



Solution:
"""
from template import *

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        arr.sort(reverse=True)
        res = ""

        def backtrack(nums, time):
            nonlocal res
            if res:
                return
            
            if not nums:
                if int(time[0: 2]) <= 23 and int(time[2::]) <= 59:
                    res = time[0: 2] + ":" + time[2::]
                return
            
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i + 1::], time + str(nums[i]))
        
        backtrack(arr, "")
        return res



"""
Question:

Given an array arr of 4 digits, find the latest 24-hour time that can be made using each digit exactly once.

24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59.

Return the latest 24-hour time in "HH:MM" format. If no valid time can be made, return an empty string.

 

Example 1:

Input: arr = [1,2,3,4]
Output: "23:41"
Explanation: The valid 24-hour times are "12:34", "12:43", "13:24", "13:42", "14:23", "14:32", "21:34", "21:43", "23:14", and "23:41". Of these times, "23:41" is the latest.
Example 2:

Input: arr = [5,5,5,5]
Output: ""
Explanation: There are no valid 24-hour times as "55:55" is not valid.
 

Constraints:

arr.length == 4
0 <= arr[i] <= 9
"""