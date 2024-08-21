"""
Title: Evaluate Reverse Polish Notation
URL: https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
Difficulty: Medium
Tags: NeetCode 150, Grind

Approach:
- want to iterate through tokens and append to stack
- we first check if the current token is in operators
- if so, we can pop the stack twice to get the values and perform the operation
- else, we just convert to int and append to stack
- lastly, the stack will have one element and we can just return that 
- TRICKS TO WATCH OUT FOR
- when popping stack, watch for order. it should be right and then left
- when doing division, make sure to wrap int() around it 
-- doing // int division DOES NOT WORK because of negative numbers. those will truncate away from zero instead of towards it.


Time Complexity: O(n)
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = "+-*/"
        for t in tokens:
            if t in operators:
                right, left = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(left + right)
                elif t == "-":
                    stack.append(left - right)
                elif t == "*":
                    stack.append(left * right)
                elif t == "/":
                    stack.append(int(left / right))
            else:
                stack.append(int(t))
        
        return stack[0]



"""
Question:

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
 

Constraints:

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
"""