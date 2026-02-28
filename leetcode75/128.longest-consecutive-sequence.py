#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()

        for num in nums:
            seen.add(num)

        res = 0
        for num in nums:
            curr_seq_len = 1
            if num - 1 not in seen: # start of a consec. seq.
                while num + 1 in seen:
                    curr_seq_len += 1
                    num += 1
            res = max(res, curr_seq_len)
        
        return res

        
# @lc code=end

