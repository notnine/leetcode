#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0 # keep track of the farthest reachable index from "this window"
        curr_end = 0 # this "window's" max reachable index
        jumps = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == curr_end:
                curr_end = farthest
                jumps += 1
        
        return jumps

# @lc code=end

