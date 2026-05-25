#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        # dp, storing the max square size for each position, as if the pos is the bottom right

        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == "0":
                    continue
                # take the min of left, top, top-left neighbor + 1
                left = dp[r][c-1] if c-1 >= 0 else 0
                top = dp[r-1][c] if r-1 >= 0 else 0
                top_left = dp[r-1][c-1] if r-1 >= 0 and c-1 >= 0 else 0
                dp[r][c] = min(left, top, top_left) + 1
                res = max(res, dp[r][c])
        
        return res*res
# @lc code=end

