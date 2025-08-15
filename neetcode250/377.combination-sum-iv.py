#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#

# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        memo = {}

        # get possible combinations, given curr running sum
        def gpc(sfs: int) -> int:
            if sfs in memo:
                return memo[sfs]
            if sfs > target:
                return 0
            if sfs == target:
                return 1
            pc = 0
            for num in nums:
                pc += gpc(sfs + num)
            memo[sfs] = pc
            return pc

        return gpc(0)
# @lc code=end

