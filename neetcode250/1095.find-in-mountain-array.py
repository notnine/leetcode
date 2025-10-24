#
# @lc app=leetcode id=1095 lang=python3
#
# [1095] Find in Mountain Array
#

# @lc code=start
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        # 1. find peak
        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2
            # if on upward slope
            if mountainArr.get(m) < mountainArr.get(m+1):
                l = m + 1
            # if on downward slope, or peak
            else:
                r = m
        peak = l # peak == l == r == m

        if mountainArr.get(peak) == target:
            return peak

        # 2. bin search in increasing part
        l, r = 0, peak - 1
        while l <= r:
            m = (l + r) // 2
            val = mountainArr.get(m)
            if val == target:
                return m
            elif val < target:
                l = m + 1
            else:
                r = m - 1

        # 3. bin search in decreasing part
        l, r = peak + 1, n - 1
        while l <= r:
            m = (l + r) // 2
            val = mountainArr.get(m)
            if val == target:
                return m
            elif val > target: # flipped because decreasing part
                l = m + 1
            else:
                r = m - 1

        return -1
# @lc code=end

