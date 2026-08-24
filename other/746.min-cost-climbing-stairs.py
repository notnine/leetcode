#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [float('inf') for _ in range(n+1)]
        dp[0] = 0
        dp[1] = 0

        for i in range(2, n+1):
            prev_two = cost[i-2] + dp[i-2]
            prev_one = cost[i-1] + dp[i-1]
            dp[i] = min(prev_two, prev_one)

        return dp[-1]
# @lc code=end

