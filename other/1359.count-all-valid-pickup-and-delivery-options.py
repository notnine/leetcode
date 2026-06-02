#
# @lc app=leetcode id=1359 lang=python3
#
# [1359] Count All Valid Pickup and Delivery Options
#

# @lc code=start
from math import comb

class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10**9 + 7
        res = 1

        for i in range(1, n+1):
            res *= comb(2*i, 2)
        
        return res % MOD 
# @lc code=end

