#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target or nums[l] == target or nums[r] == target:
                return True
            # shrink both ends if nums[l] == nums[m] == nums[r] because we can't tell which side is sorted
            elif nums[l] == nums[m] == nums[r]:
                l += 1
                r -= 1
            # if left side is sorted and target is in the left side or left side not sorted and target not in right side, search the left side
            elif (nums[l] <= nums[m] and (nums[l] < target < nums[m])) or (nums[m] <= nums[r] and not(nums[m] < target < nums[r])):
                r = m - 1
            else:
                l = m + 1
            
        return False
# @lc code=end
