#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#

# @lc code=start
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        # approach 1: pop 1 balloon and recurse
        if not nums:
            return 0

        best = 0
        n = len(nums)
        # O(n)
        for i in range(0, n):
            # pop balloon at i
            curr = 0
            if i == 0:
                if i + 1 < n:
                    curr += nums[i] * nums[i+1]
                else:
                    curr += nums[i]
            elif i == n - 1:
                if i - 1 >= 0:
                    curr += nums[i] * nums[i-1]
                else:
                    curr += nums[i]
            else:
                curr += nums[i-1] * nums[i] * nums[i+1]
            nums_without_i = nums[0:i] + nums[i+1:n]
            curr += self.maxCoins(nums_without_i) # we call maxCoins again, with n-1 length, so O(n-1)
            best = max(best, curr)
        
        # so O(n!) overall
        return best
# @lc code=end

