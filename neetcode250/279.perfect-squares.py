#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
import math

class Solution:
    def numSquares(self, n: int) -> int:
        pss = [i * i for i in range(1, int(math.sqrt(n)) + 1)]

        memo = {}

        def get_lps(sfs: int) -> int:
            if sfs in memo:
                return memo[sfs]
            if sfs > n:
                return float('inf')
            if sfs == n:
                return 0
            lps = float('inf')
            for ps in pss:
                lps = min(lps, 1 + get_lps(sfs + ps))
            memo[sfs] = lps
            return lps
        
        return get_lps(0)

        
# @lc code=end

