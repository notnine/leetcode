#
# @lc app=leetcode id=1049 lang=python3
#
# [1049] Last Stone Weight II
#

# @lc code=start
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # 0/1 knapsack / subset sum problem

        target = sum(stones) // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for w in stones:
            for s in range(target, w - 1, -1):
                dp[s] = dp[s] or dp[s - w]
        
        for s in range(target, -1, -1):
            if dp[s]:
                return (sum(stones) - s) - s
# @lc code=end

