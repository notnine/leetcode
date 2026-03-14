#
# @lc app=leetcode id=1871 lang=python3
#
# [1871] Jump Game VII
#

# @lc code=start
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [None] * n # dp[i] is True if can reach idx i
        dp[0] = True

        # loop runs O(n)
        for i in range(1, n):
            # figure out if we can reach i
            if s[i] == '1':
                continue
            
            prev_range = [None, None]
            prev_range[0] = i - maxJump
            prev_range[1] = i - minJump

            # this loop runs O(maxJump - minJump)
            for prev_idx in range(prev_range[0], prev_range[1]+1):
                if 0 <= prev_idx < n and dp[prev_idx]:
                    dp[i] = True
                    break

        return dp[n-1] if dp[n - 1] is not None else False  
# @lc code=end

