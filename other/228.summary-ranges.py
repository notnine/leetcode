#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        ranges = []
        curr_range_start = nums[0]
        curr_range_at = nums[0]

        for num in nums[1:]:
            if num == curr_range_at + 1:
                curr_range_at += 1
            else: # last range ended
                last_range = str(curr_range_start)
                if curr_range_at > curr_range_start:
                    last_range += '->' + str(curr_range_at)
                ranges.append(last_range)
                curr_range_start = num
                curr_range_at = num
        
        last_range = str(curr_range_start)
        if curr_range_at > curr_range_start:
            last_range += '->' + str(curr_range_at)
        ranges.append(last_range)
        return ranges
# @lc code=end

