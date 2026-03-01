#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i, j = 0, n - 1
        res = 0

        while i < n and j >= 0:
            curr_area = abs(i - j) * min(heights[i], heights[j])
            res = max(res, curr_area)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        
        return res   
# @lc code=end

