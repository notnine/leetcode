#
# @lc app=leetcode id=2161 lang=python3
#
# [2161] Partition Array According to Given Pivot
#

# @lc code=start
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        smaller, bigger = [], []
        pivot_count = 0

        for num in nums:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                pivot_count += 1
            else:
                bigger.append(num)
        
        res = []
        res.extend(smaller)
        res.extend([pivot for _ in range(pivot_count)])
        res.extend(bigger)
        return res
# @lc code=end

