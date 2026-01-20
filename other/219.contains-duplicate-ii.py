#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # return True if there exists a duplicate number in any window of size k + 1

        # build first window
        window = set()
        i = 0
        n = len(nums)
        while len(window) < k + 1 and i < n:
            if nums[i] in window:
                return True
            window.add(nums[i])
            i += 1
        
        while i < n:
            window.remove(nums[i - k - 1])
            if nums[i] in window:
                return True
            window.add(nums[i])
            i += 1
        
        return False
# @lc code=end

