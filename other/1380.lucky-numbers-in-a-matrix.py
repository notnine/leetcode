#
# @lc app=leetcode id=1380 lang=python3
#
# [1380] Lucky Numbers in a Matrix
#

# @lc code=start
from collections import defaultdict

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        # keep track of min of each row
        # keep track of max of each col
        # if min == max, lucky

        ROWS, COLS = len(matrix), len(matrix[0])
        row_mins, col_maxes = set(), set()

        for r in range(ROWS):
            row_mins.add(min(matrix[r]))
        
        col_to_max = defaultdict(lambda: -float('inf'))
        for r in range(ROWS):
            for c in range(COLS):
                col_to_max[c] = max(col_to_max[c], matrix[r][c])
        
        for c in col_to_max:
            col_maxes.add(col_to_max[c])
        
        return list(row_mins & col_maxes)
        
# @lc code=end

