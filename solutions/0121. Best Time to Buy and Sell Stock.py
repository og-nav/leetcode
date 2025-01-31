"""
Title: Best Time to Buy and Sell Stock
URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
Difficulty: Easy
Tags: NeetCode 150, Grind, Blind 75, Amazon, Meta, Google, Microsoft, Bloomberg, Adobe, Yahoo, Everyone
Topics: Array
Dynamic Programming

Approach:
- we want to keep track of the lowest price
- then iterate through. while iterating, if our current profit is positive, res = max(res, profit)
- but if our profit is less than 0, we know we have a lower "low" to start from
- so we can just update our min_price accordingly


Time Complexity: O(n)
Space Complexity: O(1)



Solution:
"""
from template import *

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min_price = prices[0]
        for price in prices:
            profit = price - min_price
            if profit < 0:
                min_price = price
            
            res = max(res, profit)
        
        return res



"""
Question:

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""