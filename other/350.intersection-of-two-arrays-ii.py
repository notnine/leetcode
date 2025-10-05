#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i = j = 0
        res = []
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1

            elif nums1[i] > nums2[j]:
                j += 1
            
            else:
                res.append(nums1[i])
                j, i = j + 1, i + 1

        return res

# @lc code=end

