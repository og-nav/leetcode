"""
Title: Minimum Time to Repair Cars
URL: https://leetcode.com/problems/minimum-time-to-repair-cars/
Difficulty: Medium
Tags: None
Topics: Array
Binary Search

Approach:
- create a helper function to check if all cars can be solved if given a certain time (solve formula for number of cars fixed and go through every mechanic)
- then do binary search with left pointer starting at 0 and right pointer starting at min(ranks) * cars ** 2 since potentially if one mechanic did all the work


Time Complexity: O(nlog(n))
Space Complexity: O(1)



Solution:
"""
from template import *

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        def can_repair(time):
            total_cars_fixed = 0
            for rank in ranks:
                cars_fixed = int((time / rank) ** 0.5)
                total_cars_fixed += cars_fixed
                if total_cars_fixed >= cars:
                    return True
            
            return total_cars_fixed >= cars

        l, r = 0, min(ranks) * cars ** 2 # left time, right time
        while l <= r:
            current_time = (l + r) // 2
            all_fixed = can_repair(current_time)

            if all_fixed:
                r = current_time - 1
            else:
                l = current_time + 1
        
        return l



"""
Question:

You are given an integer array ranks representing the ranks of some mechanics. ranksi is the rank of the ith mechanic. A mechanic with a rank r can repair n cars in r * n2 minutes.

You are also given an integer cars representing the total number of cars waiting in the garage to be repaired.

Return the minimum time taken to repair all the cars.

Note: All the mechanics can repair the cars simultaneously.

 

Example 1:

Input: ranks = [4,2,3,1], cars = 10
Output: 16
Explanation: 
- The first mechanic will repair two cars. The time required is 4 * 2 * 2 = 16 minutes.
- The second mechanic will repair two cars. The time required is 2 * 2 * 2 = 8 minutes.
- The third mechanic will repair two cars. The time required is 3 * 2 * 2 = 12 minutes.
- The fourth mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
It can be proved that the cars cannot be repaired in less than 16 minutes.​​​​​
Example 2:

Input: ranks = [5,1,8], cars = 6
Output: 16
Explanation: 
- The first mechanic will repair one car. The time required is 5 * 1 * 1 = 5 minutes.
- The second mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
- The third mechanic will repair one car. The time required is 8 * 1 * 1 = 8 minutes.
It can be proved that the cars cannot be repaired in less than 16 minutes.​​​​​
 

Constraints:

1 <= ranks.length <= 105
1 <= ranks[i] <= 100
1 <= cars <= 106
"""