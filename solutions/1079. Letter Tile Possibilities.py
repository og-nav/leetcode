"""
Title: Letter Tile Possibilities
URL: https://leetcode.com/problems/letter-tile-possibilities/description/
Difficulty: Medium
Tags: Google, Amazon
Topics: Hash Table
String
Backtracking
Counting

Approach:
- instead of using position and making a yes/no decision to include an item or not, we can use a counter
- and backtrack only on elements that have a positive count
- I started out building each string, but you can optimize if you realize only count matters and you don't need string


Time Complexity: O(n!)
Space Complexity: O(n) -> recursion stack can only go n deep because there are only n characters in tiles



Solution:
"""
from template import *

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = 0
        counts = defaultdict(int)
        for t in tiles:
            counts[t] += 1
        
        def backtrack(sequence_length = 0):
            nonlocal res
            if sequence_length > len(tiles):
                return
            
            if sequence_length:
                res += 1
            
            for tile in counts:
                if counts[tile] > 0:
                    counts[tile] -= 1
                    backtrack(sequence_length + 1)
                    counts[tile] += 1
        
        backtrack()
        return res




"""
Question:

You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

 

Example 1:

Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: tiles = "AAABBC"
Output: 188
Example 3:

Input: tiles = "V"
Output: 1
 

Constraints:

1 <= tiles.length <= 7
tiles consists of uppercase English letters.
"""