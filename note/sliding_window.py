"""
https://leetcode.com/tag/two-pointers/discuss/1122776/Summary-of-Sliding-Window-Patterns-for-Subarray-Substring

Sliding Window is very common in interviews and many questions that look like 
"(Longest/Shortest/Number of) (Substrings/Subarrays) with (At most/Exactly) K elements that fit (some condition)"
have a common pattern. They are usually O(n).

1. 
- we want to establish a valid and invalid state
-- for example in max consecutive ones II, https://leetcode.com/problems/max-consecutive-ones-ii/description
-- we define a valid sequence as having 1 or fewer 0s in the current sequence
-- and an invalid sequence as containing 2 0s in the current sequence

2. 
- we want to start by expanding the window until we reach an invalid state
- once we reach the invalid state, we want to contract the window by moving the left pointer until the state is valid
- then we update the "result" i.e. the longest sequence seen so far etc.
- continue expanding the window
- the result is usually of the form r - l + 1

3. 
- the structure typically looks like an outer for loop (to expand the window)
- and a nested while loop (contracting the window)
- with updating the result right after the window gets contracted

4. 
- typically will only need two pointers for simple cases
- may need to incorporate sets and hashmaps for cases like duplicates or counts

5.
- also be aware that the window size may be fixed and not variable
- in which case we need to read problem statement and try to pattern match this
- an example is 1151. Minimum Swaps to Group All 1's Together
-- the window size is fixed and would just be the total number of ones in the array
- for fixed window size, we will need to precompute the first window and then add/subtract to it while iterating through the rest of the array
-- so the code will just be two for loops right after another -> one for precomputing the state, and the second for iterating through the rest of the array
"""