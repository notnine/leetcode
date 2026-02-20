#
# @lc app=leetcode id=1812 lang=python3
#
# [1812] Determine Color of a Chessboard Square
#

# @lc code=start
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        col, row = coordinates[0], coordinates[1]

        if int(row) % 2 != 0:
            return col not in 'aceg'
        else:
            return col not in 'bdfh'     
# @lc code=end

