"""
CodeSignal-style Q3 practice problem: Matrix Diagonal Wave Sort

You are given an integer matrix.

Define each top-left to bottom-right diagonal by constant (row - col).
For every such diagonal, sort its values independently with this rule:

- If the diagonal index (row - col) is even: sort ascending
- If the diagonal index (row - col) is odd: sort descending

After sorting each diagonal, place values back on the same diagonal positions.
Return the transformed matrix.

Important details
-----------------
- Diagonals are independent; values never move across different diagonals.
- "Even/odd diagonal index" uses the signed value (row - col), which may be
  negative. Parity is still well-defined.
- Matrix can be rectangular.

Function signature
------------------
solution(matrix: List[List[int]]) -> List[List[int]]

Example
-------
matrix = [
    [8, 4, 1, 9],
    [7, 5, 2, 3],
    [6, 0, 11, 10]
]

Diagonals by (row - col):
-2: (0,2)=1, (1,3)=3                 -> even -> asc  -> [1,3]
-1: (0,1)=4, (1,2)=2, (2,3)=10       -> odd  -> desc -> [10,4,2]
 0: (0,0)=8, (1,1)=5, (2,2)=11       -> even -> asc  -> [5,8,11]
 1: (1,0)=7, (2,1)=0                 -> odd  -> desc -> [7,0]
 2: (2,0)=6                          -> even -> asc  -> [6]

Write back along each diagonal from top to bottom:
Result = [
    [5, 10, 1, 9],
    [7, 8, 4, 3],
    [6, 0, 11, 2]
]

Constraints
-----------
- 1 <= rows, cols <= 500
- 1 <= rows * cols <= 2 * 10^5
- -10^9 <= matrix[r][c] <= 10^9

Target complexity
-----------------
Let N = rows * cols.
Aim for O(N log N) total time and O(N) extra space (or better).
"""

from typing import List
from collections import defaultdict


def solution(matrix: List[List[int]]) -> List[List[int]]:
    
    ROWS, COLS = len(matrix), len(matrix[0])
    diag_to_nums = defaultdict(list)

    # collect & map all nums to its diagonals
    for r in range(ROWS):
        for c in range(COLS):
            diag = r - c
            diag_to_nums[diag].append(matrix[r][c])

    # sort
    for diag in diag_to_nums:
        if diag % 2 == 0: # even -> asc
            diag_to_nums[diag].sort()

        else: # desc
            diag_to_nums[diag].sort(reverse=True)
    
    # put sorted numbers back into matrix
    diag_to_index = defaultdict(int) # pointer to curr number of that diag

    for r in range(ROWS):
        for c in range(COLS):
            diag = r - c
            ptr = diag_to_index[diag]
            matrix[r][c] = diag_to_nums[diag][ptr]
            diag_to_index[diag] += 1
    
    return matrix

