#
# @lc app=leetcode id=343 lang=python3
#
# [343] Integer Break
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [-float('inf')] * (n+1)
        dp[1] = 1

        # for any number n, ib(n) = max(so_far, i * ib(n-i)) for all i in range(2,n)
        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * (i-j),j * dp[i-j])
        
        return dp[n]

# @lc code=end
