"""
Title: Nested List Weight Sum II
URL: https://leetcode.com/problems/nested-list-weight-sum-ii/
Difficulty: Medium
Tags: LinkedIn, Google, Amazon, Meta
Topics: Stack
Depth-First Search
Breadth-First Search

Approach:
- two pass dfs, first one gets max depth and the second one performs the calculation
- there's an issue with iterating through nestedInteger. in nested list weight sum I, I can do
-- for n in nestedList
-- but for this one I can't
- so to iterate through, use a for loop like -> for i in range(len(nestedList)) and check if nestedList[i]
-- is a list or an integer
- of note: there is a one pass solution that involves factoring out the max_depth and only applying it at the end.
-- make sure to explore this if in an interview setting. 
- can also use BFS here as well

Time Complexity: O(n) -> all elements in the nested list
Space Complexity: O(n -> height of the recursion stack



Solution:
"""
from template import *

class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        max_depth = 0
        def find_depth(nest, depth):
            nonlocal max_depth
            max_depth = max(max_depth, depth)
        
            for i in range(len(nest)):
                new_list = nest[i].getList()
                if new_list:
                    find_depth(new_list, depth + 1)

        find_depth(nestedList, 1)
        
        res = 0
        def dfs(nest, depth):
            nonlocal res
            nonlocal max_depth

            for i in range(len(nest)):
                new_list = nest[i].getList()
                if new_list:
                    dfs(new_list, depth + 1)
                else:
                    weight = max_depth - depth + 1
                    res += weight * nest[i].getInteger()
        
        dfs(nestedList, 1)
        return res



"""
Question:

You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.

The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth. Let maxDepth be the maximum depth of any integer.

The weight of an integer is maxDepth - (the depth of the integer) + 1.

Return the sum of each integer in nestedList multiplied by its weight.

 

Example 1:


Input: nestedList = [[1,1],2,[1,1]]
Output: 8
Explanation: Four 1's with a weight of 1, one 2 with a weight of 2.
1*1 + 1*1 + 2*2 + 1*1 + 1*1 = 8
Example 2:


Input: nestedList = [1,[4,[6]]]
Output: 17
Explanation: One 1 at depth 3, one 4 at depth 2, and one 6 at depth 1.
1*3 + 4*2 + 6*1 = 17
 

Constraints:

1 <= nestedList.length <= 50
The values of the integers in the nested list is in the range [-100, 100].
The maximum depth of any integer is less than or equal to 50.
There are no empty lists.
"""