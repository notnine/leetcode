#
# @lc app=leetcode id=1464 lang=python3
#
# [1464] Maximum Product of Two Elements in an Array
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if nums[0] > nums[1]:
            first_biggest = nums[0]
            second_biggest = nums[1]
        else:
            first_biggest = nums[1]
            second_biggest = nums[0]

        for num in nums[2:]:
            if first_biggest <= num:
                second_biggest = first_biggest
                first_biggest = num

            elif second_biggest <= num < first_biggest:
                second_biggest = num

        return (first_biggest - 1) * (second_biggest - 1)

# @lc code=end

