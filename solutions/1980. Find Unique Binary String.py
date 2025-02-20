"""
Title: Find Unique Binary String
URL: https://leetcode.com/problems/find-unique-binary-string/description/
Difficulty: Medium
Tags: Meta, Google, Amazon
Topics: Array
Hash Table
String
Backtracking

Approach:
- brute force is to do backtracking to generate all (or first that doesn't appear in nums)
- or you can build an answer by picking the opposite at every index while iterating thru nums
- only works for binary though, if it was like base 3 then it wouldn't work
-- for example ["000", "010", "201"], you could end up at the first index picking 2 and accidentally end up at 201 


Time Complexity: O(n)
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = []
        for i, n in enumerate(nums):
            if n[i] == "0":
                res.append("1")
            else:
                res.append("0")
        
        return "".join(res)



"""
Question:

Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

 

Example 1:

Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.
Example 2:

Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.
Example 3:

Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.
 

Constraints:

n == nums.length
1 <= n <= 16
nums[i].length == n
nums[i] is either '0' or '1'.
All the strings of nums are unique.
"""