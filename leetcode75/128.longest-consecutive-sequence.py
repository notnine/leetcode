#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        res = 1

        # check each 'starting num'
        for n in num_set:
            if n - 1 not in num_set:
                curr = 0
                while n in num_set:
                    curr += 1
                    n += 1
                res = max(res, curr)

        return res

        
# @lc code=end

