#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pos_diags = set() # (r + c)
        neg_diags = set() # (r - c)
        board = [['.'] * n for _ in range(n)] # current state, i.e we pass this during backtracking
        res = []
        
        def backtrack(row: int):
            if row == n: # append to res, each row becomes 1 string
                copied = board.copy()
                res.append(["".join(row) for row in board])
            for col in range(n):
                # if invalid pos, continue
                if (col in cols) or (row + col in pos_diags) or (row - col in neg_diags):
                    continue
                # valid pos
                cols.add(col)
                pos_diags.add(row + col)
                neg_diags.add(row - col)
                board[row][col] = 'Q'

                backtrack(row + 1)

                cols.remove(col)
                pos_diags.remove(row + col)
                neg_diags.remove(row - col)
                board[row][col] = '.'

        backtrack(0)
        return res
