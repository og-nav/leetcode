"""
Title: Combination Sum
URL: https://leetcode.com/problems/combination-sum/description/
Difficulty: Medium
Tags: NeetCode 150, Grind, Blind 75, Meta, Google, Amazon, Microsoft, Bloomberg, Apple
Topics: Array
Backtracking

Approach:
- standard backtracking but we keep track of starting index of for loop
- we need to keep track that way we don't duplicate results


Time Complexity: O(n ^ (h + 1)) -> basically height of a n-ary tree with one extra linear at the leaves to copy to res
Space Complexity: O(n ^ h)



Solution:
"""
from template import *

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(curr_nums, curr_sum, start_index):
            if curr_sum > target:
                return
            elif curr_sum == target:
                res.append(curr_nums[::])
                return
            
            for i in range(start_index, len(candidates)):
                curr_nums.append(candidates[i])
                backtrack(curr_nums, curr_sum + candidates[i], i)
                curr_nums.pop()
        
        backtrack([], 0, 0)
        return res



"""
Question:

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
 

Constraints:

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40
"""