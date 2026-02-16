#
# @lc app=leetcode id=3105 lang=python3
#
# [3105] Longest Strictly Increasing or Strictly Decreasing Subarray
#

# @lc code=start
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        i_subarr = []
        max_i = 0
        d_subarr = []
        max_d = 0

        for i, n in enumerate(nums):
            if i_subarr and i_subarr[-1] >= n:
                i_subarr = [n]
            else:
                i_subarr.append(n)
                max_i = max(max_i, len(i_subarr))
            
            if d_subarr and d_subarr[-1] <= n:
                d_subarr = [n]
            else:
                d_subarr.append(n)
                max_d = max(max_d, len(d_subarr))
        
        return max(max_i, max_d)
# @lc code=end

