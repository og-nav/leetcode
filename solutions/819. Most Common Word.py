"""
Title: Most Common Word
URL: https://leetcode.com/problems/most-common-word/description/
Difficulty: Easy
Tags: Datadog, Amazon, Google, Microsoft, Meta, Apple
Topics: Array
Hash Table
String
Counting

Approach:
- entirely a string processing question
- process string to form an array of words
- convert banned to a set
- find max count and return associated word. make sure not in banned.


Time Complexity: O(m + n) -> banned to set and then length of paragraph
Space Complexity: O(m + n) -> banned set and then counts dictionary



Solution:
"""
from template import *

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        paragraph = paragraph.lower()
        punctuation = "!?',;."
        words = []
        i = 0
        j = 0
        while i < len(paragraph):
            while i < len(paragraph) and paragraph[i] not in punctuation and paragraph[i] != ' ':
                i += 1
            words.append(paragraph[j: i])
            j = i + 1
            i += 1
        
        counts = defaultdict(int)
        for word in words:
            if word and word not in banned:
                counts[word] += 1
        
        max_value = max(counts.values())
        for k in counts:
            if counts[k] == max_value:
                return k



"""
Question:

Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.

 

Example 1:

Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.
Example 2:

Input: paragraph = "a.", banned = []
Output: "a"
 

Constraints:

1 <= paragraph.length <= 1000
paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
0 <= banned.length <= 100
1 <= banned[i].length <= 10
banned[i] consists of only lowercase English letters.
"""