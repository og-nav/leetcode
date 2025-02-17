"""
Title: Merge Two Sorted Lists
URL: https://leetcode.com/problems/merge-two-sorted-lists/description/
Difficulty: Easy
Tags: NeetCode 150, Grind, Blind 75, Google, Amazon, Meta, Bloomberg, Microsoft, Adobe, Apple
Topics: String, Stack, etc

Approach:
- dummy node
- once one list goes null, can handle appending the other one after the loop breaks


Time Complexity: O(m + n)
Space Complexity: O(1) -> res not included in space



Solution:
"""
from template import *

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(None)
        copy = res
        while list1 and list2:
            if list1.val < list2.val:
                copy.next = list1
                list1 = list1.next
            else:
                copy.next = list2
                list2 = list2.next
            
            copy = copy.next
        
        if list1:
            copy.next = list1
        else:
            copy.next = list2
        
        return res.next



"""
Question:

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""