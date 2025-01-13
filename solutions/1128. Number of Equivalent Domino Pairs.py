"""
Title: Number of Equivalent Domino Pairs
URL: https://leetcode.com/problems/number-of-equivalent-domino-pairs/
Difficulty: Easy
Tags: None
Topics: Array
Hash Table
Counting

Approach:
- very tricky and very deceptive
- want to use a counter hashmap, and make sure to sort each domino to avoid needless if statements
- then afterwards, want to make a second pass where if the count is greater than 1, we apply the 
-- summation formula but with minus instead of plus


Time Complexity: O(n)
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        d = defaultdict(int)
        res = 0
        for domino in dominoes:
            c = tuple(sorted(domino))
            d[c] += 1
        
        for k in d:
            if d[k] > 1:
                res += (d[k] ** 2 - d[k]) // 2
        
        return res



"""
Question:

Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

 

Example 1:

Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1
Example 2:

Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
Output: 3
 

Constraints:

1 <= dominoes.length <= 4 * 104
dominoes[i].length == 2
1 <= dominoes[i][j] <= 9
"""