"""
Title: Product of Last K Numbers
URL: https://leetcode.com/problems/product-of-the-last-k-numbers/description/
Difficulty: Medium
Tags: Meta, Amazon, TikTok, Google, Apple, Target
Topics: Array
Math
Design
Data Stream
Prefix Sum

Approach:
- we need to keep a "prefix product" array with dummy 1 to start
- we also need to realize what happens when we encounter a 0 in the stream
-- if we have a 0, we need to notice that any k greater than the 0 position will automatically result in a 0 product
--- therefore, we can reset our prefix product to the default
- then in getProduct, just need to check if k is greater than or equal to the length of our prefix product
-- and if so, we know that we had to reset the product array, so we just return 0 per the observation above
-- else, we can do the basic prefix sum operation where we take the right element and divide it by the left element


Time Complexity: O(1) -> all functions are implemented in O(1) time, so overall time complexity including the stream would be O(n) where n is the length of the stream
Space Complexity: O(n) -> may not encounter any 0s so we may end up storing all n stream items in the prefix product array



Solution:
"""
from template import *

class ProductOfNumbers:

    def __init__(self):
        self.prefix_product = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix_product = [1]
            return
        
        self.prefix_product.append(self.prefix_product[-1] * num)
        

    def getProduct(self, k: int) -> int:
        # encountered a 0 previously and had to reset array
        if k >= len(self.prefix_product): 
            return 0
        
        return self.prefix_product[-1] // self.prefix_product[-k - 1]



"""
Question:

Design an algorithm that accepts a stream of integers and retrieves the product of the last k integers of the stream.

Implement the ProductOfNumbers class:

ProductOfNumbers() Initializes the object with an empty stream.
void add(int num) Appends the integer num to the stream.
int getProduct(int k) Returns the product of the last k numbers in the current list. You can assume that always the current list has at least k numbers.
The test cases are generated so that, at any time, the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing.

 

Example:

Input
["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
[[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]

Output
[null,null,null,null,null,null,20,40,0,null,32]

Explanation
ProductOfNumbers productOfNumbers = new ProductOfNumbers();
productOfNumbers.add(3);        // [3]
productOfNumbers.add(0);        // [3,0]
productOfNumbers.add(2);        // [3,0,2]
productOfNumbers.add(5);        // [3,0,2,5]
productOfNumbers.add(4);        // [3,0,2,5,4]
productOfNumbers.getProduct(2); // return 20. The product of the last 2 numbers is 5 * 4 = 20
productOfNumbers.getProduct(3); // return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
productOfNumbers.getProduct(4); // return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
productOfNumbers.add(8);        // [3,0,2,5,4,8]
productOfNumbers.getProduct(2); // return 32. The product of the last 2 numbers is 4 * 8 = 32 
 

Constraints:

0 <= num <= 100
1 <= k <= 4 * 104
At most 4 * 104 calls will be made to add and getProduct.
The product of the stream at any point in time will fit in a 32-bit integer.
 

Follow-up: Can you implement both GetProduct and Add to work in O(1) time complexity instead of O(k) time complexity?

"""