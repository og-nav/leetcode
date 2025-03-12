"""
Title: Reorganize String
URL: https://leetcode.com/problems/reorganize-string/description/
Difficulty: Medium
Tags: Amazon, Google, Roblox, Meta, TikTok, Microsoft, Pinterest, Adobe, Apple, Bloomberg
Topics: Hash Table
String
Greedy
Sorting
Heap (Priority Queue)
Counting

Approach:
- counter into max heap
- while heap has more than 2 elements, we want to greedily add the top 2 most frequent letters to the result
- only one of each though because we may need to use some later. then just decrement/increment count and only push to heap if count is > 0


Time Complexity: O(nlog(k)) -> k is 26 so one could argue time complexity is only n
Space Complexity: O(k) -> heap and counter only hold 26 characters at most so could also argue that it is O(1)



Solution:
"""
from template import *

class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1
        
        # max heap
        heap = [(-counts[c], c) for c in counts]
        heapq.heapify(heap)
        
        res = []
        while len(heap) >= 2:
            a_count, a = heapq.heappop(heap)
            b_count, b = heapq.heappop(heap)

            res.append(a)
            res.append(b)
            
            if b_count < -1:
                heapq.heappush(heap, (b_count + 1, b))
            if a_count < -1:
                heapq.heappush(heap, (a_count + 1, a))
        
        # might be one element left in heap
        if len(heap) == 1:
            if abs(heap[0][0]) > 1:
                return ""
            res.append(heap[0][1])
        
        return "".join(res)



"""
Question:

Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

 

Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
"""