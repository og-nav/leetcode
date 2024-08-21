"""
Title: Dot Product of Two Sparse Vectors
URL: https://leetcode.com/problems/dot-product-of-two-sparse-vectors/description/
Difficulty: Medium
Tags: NeetCode 150, Grind, Meta

Approach:
1. Hashmap (naive)
- data structure is a hashmap where key is index and value is the value in nums
- need to populate hashmap in init function itself
- then for dot product, just iterate through self.sv and get vec's value if it exists

- downside is that hashmaps take time to set up
- hashmap might be far away in memory whereas elements in an array are contiguous

2. Two pointer
- populate a pairs array with pairs of (index, value) arrays
- then use two pointers (while a < len(self.pairs) and b < len(vec.pairs))
- then 3 cases -> 
  1. if self.pairs[a][0] == vec.pairs[b][0]: add to result and increment a and b
  2. if self.pairs[a][0] < vec.pairs[b][0]: increment a
  3. else: increment b

Follow up: What if only one of the vectors is sparse?
- we still process both vectors into the pairs array
- then we can iterate through sparse array and perform binary search on full array


Time Complexity: O(min(n, m))
Space Complexity: O(n + m)
both for both



Solution:
"""
from template import *

# 1. Hashmap
class SparseVector:
    def __init__(self, nums: List[int]):
        self.sv = defaultdict(int)

        for i, n in enumerate(nums):
            if n:
                self.sv[i] = n

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for i in self.sv:
            res += self.sv[i] * vec.sv[i]

        return res
    

# 2. Two Pointer
class SparseVector:
    def __init__(self, nums: List[int]):
        self.pairs = []

        for i, n in enumerate(nums):
            if n:
                self.pairs.append([i, n])

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        a, b = 0, 0
        while a < len(self.pairs) and b < len(vec.pairs):
            if self.pairs[a][0] == vec.pairs[b][0]:
                res += self.pairs[a][1] * vec.pairs[b][1]
                a += 1
                b += 1
            elif self.pairs[a][0] < vec.pairs[b][0]:
                a += 1
            else:
                b += 1
        
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)





"""
Question:

Given two sparse vectors, compute their dot product.

Implement class SparseVector:

SparseVector(nums) Initializes the object with the vector nums
dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

Follow up: What if only one of the vectors is sparse?

 

Example 1:

Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
Output: 8
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8
Example 2:

Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
Output: 0
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0
Example 3:

Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
Output: 6
 

Constraints:

n == nums1.length == nums2.length
1 <= n <= 10^5
0 <= nums1[i], nums2[i] <= 100
"""