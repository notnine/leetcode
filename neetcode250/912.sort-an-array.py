#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#

# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n < 2:
            return nums

        nums1 = nums[:n // 2]
        nums2 = nums[n // 2:]
        nums1 = self.sortArray(nums1)
        nums2 = self.sortArray(nums2)
        res = []
        i, j = 0,0
        while (i + j) < n:
            if i == len(nums1):
                res.extend(nums2[j:])
                return res
            if j == len(nums2):
                res.extend(nums1[i:])
                return res
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        return res

        
# @lc code=end

