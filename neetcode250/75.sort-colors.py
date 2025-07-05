#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        i = 0

        def swap(p1: int, p2: int) -> None:
            nums[p1], nums[p2] = nums[p2], nums[p1]
        
        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
                i += 1
            elif nums[i] == 2:
                swap(r, i)
                r -= 1
            else:
                i += 1
        

# @lc code=end

