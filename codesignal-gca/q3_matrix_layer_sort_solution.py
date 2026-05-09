"""
CodeSignal-style Q3 practice problem: Matrix Layer Sort

You are given a rectangular matrix of integers.
The matrix has concentric "layers" (also called rings):
- layer 0 is the outer border
- layer 1 is the border just inside layer 0
- and so on

For each layer, do the following independently:
1) Traverse the layer in clockwise border order:
   - top row (left -> right)
   - right column (top+1 -> bottom-1)
   - bottom row (right -> left), if top < bottom
   - left column (bottom-1 -> top+1), if left < right
2) Collect all values from that layer.
3) Sort those values in ascending order.
4) Write sorted values back into the same layer positions in the same traversal
   order.

Return the transformed matrix after processing all layers.

Notes
-----
- Each layer is sorted independently.
- The relative positions between different layers do not mix.
- If the matrix has a center row/column/cell with no full border
  (e.g. odd dimensions), it is still considered the innermost layer:
  collect its positions by the same traversal rules and sort them.

Function signature
------------------
solution(matrix: List[List[int]]) -> List[List[int]]

Example
-------
matrix = [
    [9, 8, 7, 6],
    [5, 1, 2, 4],
    [3, 0, 10, 11],
    [12, 13, 14, 15]
]

Layer 0 positions in traversal order:
(0,0)(0,1)(0,2)(0,3)(1,3)(2,3)(3,3)(3,2)(3,1)(3,0)(2,0)(1,0)
Values: [9,8,7,6,4,11,15,14,13,12,3,5]
Sorted: [3,4,5,6,7,8,9,11,12,13,14,15]

Layer 1 positions:
(1,1)(1,2)(2,2)(2,1)
Values: [1,2,10,0]
Sorted: [0,1,2,10]

Result:
[
    [3, 4, 5, 6],
    [15, 0, 1, 7],
    [14, 10, 2, 8],
    [13, 12, 11, 9]
]

Constraints
-----------
- 1 <= rows, cols <= 500
- 1 <= rows * cols <= 2 * 10^5
- -10^9 <= matrix[r][c] <= 10^9

Target complexity
-----------------
Let N = rows * cols.
Aim for O(N log N) in total (or better), with O(N) extra space.
"""

from typing import List


def solution(matrix: List[List[int]]) -> List[List[int]]:
    ROWS, COLS = len(matrix), len(matrix[0])

    top_row, bottom_row = 0, ROWS - 1
    left_col, right_col = 0, COLS - 1

    while top_row <= bottom_row and left_col <= right_col:
        nums = []

        # gather all the numbers in this layer
        for c in range(left_col, right_col + 1):
            nums.append(matrix[top_row][c])
        
        for r in range(top_row + 1, bottom_row + 1):
            nums.append(matrix[r][right_col])
        
        if bottom_row != top_row:
            for c in range(left_col, right_col):
                nums.append(matrix[bottom_row][c])
        
        if left_col != right_col:
            for r in range(top_row + 1, bottom_row):
                nums.append(matrix[r][left_col])

        # sort
        nums.sort()
        i = 0

        # put them back into the layer
        for c in range(left_col, right_col + 1):
            matrix[top_row][c] = nums[i]
            i += 1
        
        for r in range(top_row + 1, bottom_row + 1):
            matrix[r][right_col] = nums[i]
            i += 1
        
        if top_row != bottom_row:
            for c in range(right_col - 1, left_col - 1, - 1):
                matrix[bottom_row][c] = nums[i]
                i += 1
        
        if left_col != right_col:
            for r in range(bottom_row - 1, top_row, - 1):
                matrix[r][left_col] = nums[i]
                i += 1

        # update top_row, bottom_row, left_col, right_col
        top_row += 1
        bottom_row -= 1
        left_col += 1
        right_col -= 1

    return matrix