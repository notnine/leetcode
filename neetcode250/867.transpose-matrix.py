#
# @lc app=leetcode id=867 lang=python3
#
# [867] Transpose Matrix
#

# @lc code=start
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(matrix), len(matrix[0])
        res = [[0 for _ in range(ROWS)] for _ in range(COLS)]

        for i in range(ROWS):
            for j in range(COLS):
                res[j][i] = matrix[i][j]
        
        return res
# @lc code=end

