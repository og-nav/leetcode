"""
Title: Next Closest Time
URL: https://leetcode.com/problems/next-closest-time/description/
Difficulty: Medium
Tags: Google
Topics: Hash Table
String
Backtracking
Enumeration

Approach:
- brute force backtracking to put all possible permutations into a set
- then converted set to list and sorted
- then returned the next element in the list after the current time (wrapping around to beginning if needed)
- make sure if statement in backtrack makes sure the hours are under 24 instead of 25


Time Complexity: O(1) -> but only technically since we only have 4 digits. the actual number is 4 ^ 4 I believe
Space Complexity: O(1) -> same, I think actual number would be 4 ^ 4 possible permutations



Solution:
"""
from template import *

class Solution:
    def nextClosestTime(self, time: str) -> str:
        candidates = set()
        digits = [time[0], time[1], time[3], time[4]]
        def backtrack(curr):
            if len(curr) == 4:
                if int(curr[0: 2]) < 24 and int(curr[2::]) < 60:
                    candidates.add(curr[0: 2] + ":" + curr[2::])
                return
            
            for digit in digits:
                backtrack(curr + digit)
        
        backtrack("")
        candidates = list(candidates)
        candidates.sort()
        for i in range(len(candidates)):
            if candidates[i] == time:
                return candidates[(i + 1) % len(candidates)]



"""
Question:

Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

 

Example 1:

Input: time = "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.
It is not 19:33, because this occurs 23 hours and 59 minutes later.
Example 2:

Input: time = "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22.
It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.
 

Constraints:

time.length == 5
time is a valid time in the form "HH:MM".
0 <= HH < 24
0 <= MM < 60
"""