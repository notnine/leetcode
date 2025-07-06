#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#

# @lc code=start
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.matrix = [[0 for _ in range(COLS + 1)] for _ in range(ROWS + 1)]

        # calculate prefix matrices
        for r in range(1, ROWS + 1):
            for c in range(1, COLS + 1):
                self.matrix[r][c] = self.matrix[r-1][c] + self.matrix[r][c-1] + matrix[r-1][c-1] - self.matrix[r-1][c-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = self.matrix[row2+1][col2+1]

        # subtract bottom left side sub matrix from whole matrix
        res -= self.matrix[row2+1][col1]

        # subtract top right side sub matrix from whole matrix
        res -= self.matrix[row1][col2+1]

        # we subtracted top left sub matrix twice, so re-add once
        res += self.matrix[row1][col1]

        return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end
