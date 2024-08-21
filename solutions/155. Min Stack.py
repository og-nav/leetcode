"""
Title: Min Stack
URL: https://leetcode.com/problems/min-stack/description/
Difficulty: Medium
Tags: NeetCode 150, Grind

Approach:
- instead of saving only the value, save a tuple of the value and the previous minimum
- the class variables are just an empty array for the stack and the "previous" minimum value (set to float('inf'))
- for push, we just append the val and the current min
- for pop, we pop and check the values
-- if the value popped is equal to the current min_value (we got rid of the smallest value),
--- we set the current min_value to the previous min_val
- top and getMin are straightforward, we just access/return the class variables


Time Complexity: O(1)
Space Complexity: O(n)



Solution:
"""
from template import *

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_value = float('inf')

    def push(self, val: int) -> None:
        self.stack.append((val, self.min_value)) # (current value, previous min value)
        if val < self.min_value:
            self.min_value = val

    def pop(self) -> None:
        val, prev = self.stack.pop()
        if val == self.min_value:
            self.min_value = prev

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.min_value


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()



"""
Question:

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.
"""