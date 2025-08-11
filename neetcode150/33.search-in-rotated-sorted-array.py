#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target: return m
            elif nums[l] == target: return l
            elif nums[r] == target: return r
            
            # search in the left part
            # if left part sorted and target in left range, or, left part not sorted and (target < nums[m] or target > nums[l])
            elif (nums[l] < nums[m] and nums[l] <= target < nums[m]) or (nums[l] > nums[m] and (target < nums[m] or target > nums[l])):
                r = m - 1
            
            # search in the right part
            else:
                l = m + 1

        return -1
# @lc code=end

