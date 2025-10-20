#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#

# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        # return whether we can split nums into k subarrays, where the max([sum(subarr) for each subarr]) <= x
        def can_split(x: int) -> bool:
            # greedily maximize curr subarr until its sum is > x, then create a new subarr starting at nums[i]
            subarrs = 0
            running_sum = 0
            for num in nums:
                if running_sum + num > x:
                    subarrs += 1
                    running_sum = num
                else:
                    running_sum += num
            # last subarr is not yet counted in subarrs
            subarrs += 1
            return subarrs <= k
        
        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            m = (l + r) // 2
            if can_split(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res


# @lc code=end

