#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        pos_diags = set()
        neg_diags = set()
        res = 0

        def backtrack(row: int):
            nonlocal res

            if row == n:
                res += 1
                return

            for col in range(n):
                if col not in cols and (row - col) not in neg_diags and (row + col) not in pos_diags:
                    cols.add(col)
                    neg_diags.add(row - col)
                    pos_diags.add(row + col)
                    backtrack(row + 1)
                    cols.remove(col)
                    neg_diags.remove(row - col)
                    pos_diags.remove(row + col)
        
        backtrack(0)
        return res
# @lc code=end

