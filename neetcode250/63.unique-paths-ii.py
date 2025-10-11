#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        dp = {} # dp[(i, j)] stores num of possible paths from pos (i, j)

        # return num paths possible to bottom right from pos (i, j)
        def get_paths(i: int, j: int) -> int:
            if (i, j) in dp:
                return dp[(i, j)]
            # if out of bounds or obstacle
            if i >= ROWS or j >= COLS or obstacleGrid[i][j] == 1:
                return 0
            # if reach bottom right
            if i == ROWS - 1 and j == COLS - 1:
                return 1
            
            dp[(i, j)] = get_paths(i, j + 1) + get_paths(i + 1, j)
            return dp[(i, j)]

        return get_paths(0, 0)
# @lc code=end

