"""
Title: Moving Average from Data Stream
URL: https://leetcode.com/problems/moving-average-from-data-stream/description/
Difficulty: Easy
Tags: Meta, Google, Amazon, Spotify
Topics: Array
Design
Queue
Data Stream

Approach:
- use a queue to store all elements. pop if len(queue) is greater than size
- keep a running sum


Time Complexity: O(1) -> each operation is O(1) for each query
Space Complexity: O(n) -> where n is the size



Solution:
"""
from template import *

class MovingAverage:

    def __init__(self, size: int):
        self.window = deque()
        self.running_sum = 0
        self.size = size

    def next(self, val: int) -> float:
        self.window.append(val)
        self.running_sum += val

        if len(self.window) > self.size:
            removed = self.window.popleft()
            self.running_sum -= removed
            return self.running_sum / self.size
        
        return self.running_sum / len(self.window)



"""
Question:


"""