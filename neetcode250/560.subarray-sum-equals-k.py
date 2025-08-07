#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = defaultdict(int) # frequency map
        prefix_sums[0] += 1
        res = 0
        curr = 0 # running sum

        for n in nums:
            curr += n
            if (k - n) in prefix_sums:
                res += prefix_sums[k-n]

        return res


# @lc code=end

