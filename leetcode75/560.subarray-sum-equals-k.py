#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = [0] # prefix_sums[i] holds sum(nums[:i])
        for n in nums:
            curr = prefix_sums[-1] + n
            prefix_sums.append(curr)

        # do we need this
        b_prefix_sums = [0] # b_prefix_sums[i] holds sum(nums[len(nums)-i:])
        for n in nums[::-1]:
            curr = prefix_sums[-1] + n
            prefix_sums.append(curr)

        # check sum of all sub arrays
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i, n):
                # get sum(nums[i:j+1])
                if prefix_sums[j+1] - prefix_sums[i] == k:
                    res += 1

        return res
        
# @lc code=end

