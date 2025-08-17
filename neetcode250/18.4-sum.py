#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # run 3sum
            for j in range(i + 1, n):

                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # run 2sum
                curr_target = target - (nums[j] + nums[i])
                l, r = j + 1, n - 1
                while l < r:
                    
                    curr = nums[l] + nums[r]
                    if curr < curr_target:
                        l += 1
                    elif curr > curr_target:
                        r -= 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1

                    while l > j + 1 and l < r and nums[l] == nums[l - 1]:
                        l += 1
        
        return res

# @lc code=end

