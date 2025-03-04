"""
Title: Fruits Into Baskets
URL: https://leetcode.com/problems/fruit-into-baskets/description/
Difficulty: Medium
Tags: Meta, Google, Amazon, Microsoft
Topics: Array
Hash Table
Sliding Window

Approach:
- problem is basically largest subarray that contains at most two elements
- so we need to use a hashmap to keep track of the window size
- to move the left pointer, just keep decrementing fruits until one reaches 0
- the fruit to remove doesn't necessarily need to be the left-most fruit in the window (trap I fell into my first time trying this)


Time Complexity: O(n)
Space Complexity: O(1)



Solution:
"""
from template import *

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # basically need to find the largest subarray that only contains two elements
        res = 0
        l = 0
        basket = defaultdict(int)

        for r in range(len(fruits)):
            # add fruit to basket
            basket[fruits[r]] += 1

            # if state is invalid, shrink the window
            # delete first fruit that makes the window valid again
            # doesn't have to be the left-most fruit
            while len(basket) > 2:
                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]
                l += 1
            
            res = max(res, r - l + 1)
        
        return res



"""
Question:

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

 

Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
 

Constraints:

1 <= fruits.length <= 105
0 <= fruits[i] < fruits.length
"""