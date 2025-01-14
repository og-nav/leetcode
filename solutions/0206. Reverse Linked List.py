"""
Title: Reverse Linked List
URL: https://leetcode.com/problems/reverse-linked-list/description/
Difficulty: Easy
Tags: NeetCode 150, Grind, Blind 75

Approach:
- make sure to initialize prev to None
- then it's just pointer gymnastics in the right order to rearrange head's pointers to the right nodes
- then return prev
- follow up: did not understand. make sure to study.


Time Complexity: O(n)
Space Complexity: O(1)



Solution:
"""
from template import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        
        return prev
    
    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return node



"""
Question:

Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""