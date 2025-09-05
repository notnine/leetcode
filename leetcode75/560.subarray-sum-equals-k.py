#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        running_sum = 0 
        res = 0
        presum_to_count = defaultdict(int)
        presum_to_count[0] = 1
        for n in nums:
            running_sum = running_sum + n
            if running_sum - k in presum_to_count:
                res += presum_to_count[running_sum - k]
            presum_to_count[running_sum] += 1

        return res
        
# @lc code=end

