"""
Title: Asteroid Collision
URL: https://leetcode.com/problems/asteroid-collision/
Difficulty: Medium
Tags: Grind, Amazon, Google, Microsoft, Meta, DoorDash, Apple, Oracle, Bloomberg
Topics: Array
Stack
Simulation

Approach:
- edge case nightmare
- use stack, but need to watch out for every edge case since actions are different if asteroids are same or different magnitudes
- double check with following test cases
- [-2,-1,1,2]
- [-2,-2,1,-2]
- [-2,-2,1,-1]

Time Complexity: O(n)
Space Complexity: O(n)



Solution:
"""
from template import *

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if a < 0:
                if not stack or stack[-1] < 0:
                    stack.append(a)
                else:
                    while stack and stack[-1] > 0:
                        if stack[-1] < abs(a):
                            stack.pop()
                        elif stack[-1] == abs(a):
                            stack.pop()
                            break
                        else:
                            break
                    else:
                        stack.append(a)
            else:
                stack.append(a)
        
        return stack



"""
Question:

We are given an array asteroids of integers representing asteroids in a row. The indices of the asteriod in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
 

Constraints:

2 <= asteroids.length <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
"""