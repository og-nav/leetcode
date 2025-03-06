"""
Title: Find the Town Judge
URL: https://leetcode.com/problems/find-the-town-judge/description/
Difficulty: Easy
Tags: Google, Amazon, Microsoft, Adobe, Bloomberg, Apple
Topics: Array
Hash Table
Graph

Approach:
- check indegree and outdegree and build candidates list then find the judge
- interviewer may not explicitly tell you that there is only 1 town judge - you will need to ask
-- and if they ask you if it's possible to have more than two -> it is actually impossible!
--- because they would have to trust each other because the rules say that the town judge must be trusted by everyone else


Time Complexity: O(n)
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        sent_trust = [0] * n
        received_trust = [0] * n

        for a, b in trust:
            sent_trust[a - 1] += 1
            received_trust[b - 1] += 1
        
        candidates = []
        for i in range(len(sent_trust)):
            if sent_trust[i] == 0:
                candidates.append(i)
        
        for candidate in candidates:
            if received_trust[candidate] == n - 1:
                return candidate + 1
        
        return -1



"""
Question:

In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

 

Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
 

Constraints:

1 <= n <= 1000
0 <= trust.length <= 104
trust[i].length == 2
All the pairs of trust are unique.
ai != bi
1 <= ai, bi <= n
"""