"""
Title: Number of Substrings Containing All Three Characters
URL: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/
Difficulty: Medium
Tags: Meta, Google, Amazon, Bloomberg, Microsoft
Topics: Hash Table
String
Sliding Window

Approach:
- regular sliding window with a variation in how the result is updated
- once we find a valid substring that contains all three characters, then any additional characters added from the right side of the window will still keep the window valid
- therefore, we need to increase the result by the length of the string minus the right pointer while we move the left pointer


Time Complexity: O(n)
Space Complexity: O(1)



Solution:
"""
from template import *

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        window = defaultdict(int)
        res = 0
        l = 0

        for r in range(len(s)):
            # add to window
            window[s[r]] += 1

            while len(window) == 3:
                # all substrings from here to the end are valid
                res += len(s) - r
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                
                l += 1
        
        return res



"""
Question:

Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
Example 3:

Input: s = "abc"
Output: 1
 

Constraints:

3 <= s.length <= 5 x 10^4
s only consists of a, b or c characters.
"""