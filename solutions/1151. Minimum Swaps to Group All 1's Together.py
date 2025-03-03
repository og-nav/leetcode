"""
Title: Minimum Swaps to Group All 1's Together
URL: https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/description/
Difficulty: Medium
Tags: TikTok, Microsoft
Topics: Array
Sliding Window

Approach:
- standard sliding window
- window size is fixed and is just the total number of ones in the array


Time Complexity: O(n)
Space Complexity: O(1)



Solution:
"""
from template import *

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        # fixed sized window
        # our window size should be the total number of ones in the array
        window_size = 0
        for n in data:
            window_size += n
        
        if window_size <= 1:
            return 0
        
        # calculate initial window
        res = len(data)
        ones = 0
        for i in range(window_size):
            ones += data[i]
        res = min(res, window_size - ones)

        for i in range(window_size, len(data)):
            # move the window to the right
            ones += data[i]
            ones -= data[i - window_size]
            res = min(res, window_size - ones)
        
        return res



"""
Question:

Given a binary array data, return the minimum number of swaps required to group all 1’s present in the array together in any place in the array.

 

Example 1:

Input: data = [1,0,1,0,1]
Output: 1
Explanation: There are 3 ways to group all 1's together:
[1,1,1,0,0] using 1 swap.
[0,1,1,1,0] using 2 swaps.
[0,0,1,1,1] using 1 swap.
The minimum is 1.
Example 2:

Input: data = [0,0,0,1,0]
Output: 0
Explanation: Since there is only one 1 in the array, no swaps are needed.
Example 3:

Input: data = [1,0,1,0,1,0,0,1,1,0,1]
Output: 3
Explanation: One possible solution that uses 3 swaps is [0,0,0,0,0,1,1,1,1,1,1].
 

Constraints:

1 <= data.length <= 105
data[i] is either 0 or 1.
"""