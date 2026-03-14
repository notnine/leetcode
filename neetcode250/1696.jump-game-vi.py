#
# @lc app=leetcode id=1696 lang=python3
#
# [1696] Jump Game VI
#

# @lc code=start
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [None] * n # dp[i] is True if can reach last indx from i
        dp[n - 1] = True

        # return True if can reach last idx from i
        def dfs(i: int) -> bool:
            if dp[i] is not None:
                return dp[i]
            
            for j in range(minJump, min(maxJump + 1, n - i)):
                if s[i + j] == '0':
                    if dfs(i + j):
                        dp[i + j] = True
                        return True
                    else:
                        continue

            dp[i] = False
            return False

        return dfs(0)# @lc code=end

