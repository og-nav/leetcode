"""
Title: Toeplitz Matrix
URL: https://leetcode.com/problems/toeplitz-matrix/description/
Difficulty: Easy

Approach:
- just check if matrix[i - 1][j - 1] is equal to matrix[i][j] for every square in matrix
- needs one condition to make sure that i > 0 and j > 0 to make sure we stay in matrix


Time Complexity: O(m * n)
Space Complexity: O(1)



Solution:
"""
from template import *

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i > 0 and j > 0 and matrix[i][j] != matrix[i - 1][j - 1]:
                    return False
        
        return True



"""
Question:

Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

 

Example 1:


Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
Example 2:


Input: matrix = [[1,2],[2,2]]
Output: false
Explanation:
The diagonal "[1, 2]" has different elements.
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 20
0 <= matrix[i][j] <= 99
"""