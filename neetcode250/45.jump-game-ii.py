#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')] * len(nums) # where dp[i] represents min num to reach final index from i
        dp[len(nums) - 1] = 0 # 0 steps to reach final index from final index

        # iterate from 2nd last index, calculating min steps for each index
        for i in range(len(nums) - 2, -1, -1):
            steps = nums[i] # can jump steps from index i
            so_far = float('inf') # min steps to last index seen so far
            for add in range(0, steps + 1):
                if i + add < len(nums):
                    so_far = min(so_far, 1 + dp[i + add])
            dp[i] = so_far

        return dp[0]
# @lc code=end

