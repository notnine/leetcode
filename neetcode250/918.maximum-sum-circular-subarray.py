#
# @lc app=leetcode id=918 lang=python3
#
# [918] Maximum Sum Circular Subarray
#

# @lc code=start
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        
        # the max sum sub arr is either a contiguous block, or a warped sub arr. 
        # we can find the max sub arr in both cases, and return the max of the two.

        # edge case: if all negative
        if max(nums) < 0:
            return max(nums)

        # 1. find max sub arr in contiguous block (normal kadane's)
        max_sub_arr = nums[0] if nums[0] > 0 else 0
        curr_sub_arr = nums[0] if nums[0] > 0 else 0
        for i in range(1, n):
            curr_sub_arr = max(0, curr_sub_arr + nums[i]) # basically start sub arr over if sub arr negative
            max_sub_arr = max(curr_sub_arr, max_sub_arr)
        max_contiguous_sub_arr = max_sub_arr

        # 2. find max warped sub arr (sum(nums) - minimum contiguous sub arr) use kadane's to find min sub arr
        min_sub_arr = nums[0] if nums[0] < 0 else 0
        curr_sub_arr = nums[0] if nums[0] < 0 else 0
        for i in range(1, n):
            curr_sub_arr = min(0, curr_sub_arr + nums[i])
            min_sub_arr = min(curr_sub_arr, min_sub_arr)
        max_warped_sub_arr = sum(nums) - min_sub_arr

        # 3. return max from each case
        return max(max_contiguous_sub_arr, max_warped_sub_arr)
# @lc code=end

