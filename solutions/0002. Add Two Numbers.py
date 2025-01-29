"""
Title: Add Two Numbers
URL: https://leetcode.com/problems/add-two-numbers/description/
Difficulty: Medium
Tags: NeetCode 150, Grind, Google, Meta, Amazon, Bloomberg, Microsoft, Apple, Adobe, Uber, Yahoo, Nvidia
Topics: String, Stack, etc

Approach:
- as of this writing, my natural approach is to iterate through each list and put them into their own arrays
-- then go digit by digit to add them up
-- and then take care of array length mismatch 
-- and then create a new list
- but it is possible to do it in constant space (build new list while using up input lists)
-- like iterate through each list, but once a list runs out, just add 0 instead of breaking and doing the checks
- if reading this in prep for an interview, make sure to try solving it that way. this question is very popular


Time Complexity: O(max(m, n))
Space Complexity: O(max(m, n))



Solution:
"""
from template import *

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        while l1:
            a.append(l1.val)
            l1 = l1.next
        
        b = []
        while l2:
            b.append(l2.val)
            l2 = l2.next
        
        i = 0
        j = 0
        res = []
        carry = 0
        while i < len(a) and j < len(b):
            digit = a[i] + b[j] + carry
            res.append(digit % 10)
            carry = digit > 9

            i += 1
            j += 1
        
        if len(a) > len(b):
            for k in range(len(b), len(a)):
                digit = a[k] + carry
                res.append(digit % 10)
                carry = digit > 9
        elif len(b) > len(a):
            for k in range(len(a), len(b)):
                digit = b[k] + carry
                res.append(digit % 10)
                carry = digit > 9
        if carry:
            res.append(1)
        
        head = ListNode(0)
        copy = head
        for k in range(len(res)):
            copy.next = ListNode(res[k], None)
            copy = copy.next
        
        return head.next



"""
Question:

ou are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""