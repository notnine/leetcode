#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        memo = {}

        # return min path from pos (i, j)
        def get_min(i: int, j: int) -> int:
            if (i, j) in memo:
                return memo[(i, j)]

            if i == ROWS - 1 and j == COLS - 1:
                return grid[i][j]

            # go down if down is in bounds
            down_i, down_j = i + 1, j
            if down_i < ROWS and down_j < COLS:
                go_down = get_min(down_i, down_j)
            else:
                go_down = float('inf')
            
            # go right if right is in bounds
            right_i, right_j = i, j + 1
            if right_i < ROWS and right_j < COLS:
                go_right = get_min(right_i, right_j)
            else:
                go_right = float('inf')
            
            memo[(i, j)] = min(go_right, go_down) + grid[i][j]
            return memo[(i, j)]
            
        return get_min(0, 0)
# @lc code=end

