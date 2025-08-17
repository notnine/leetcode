#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if i > 0 and nums[i-1] == nums[i]: # we've looked at this number
                continue

            l, r = i + 1, n - 1
            # 2sum, look for elements that add up to -(nums[i])
            target = -(nums[i])
            while l < r:
                two_sum = nums[l] + nums[r]
                if two_sum < target:
                    l += 1
                elif two_sum > target:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                # skip the numbers we've looked at
                while l < r and l > i + 1 and nums[l] == nums[l - 1]:
                    l += 1

        return res

# @lc code=end

