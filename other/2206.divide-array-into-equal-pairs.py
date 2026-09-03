#
# @lc app=leetcode id=2206 lang=python3
#
# [2206] Divide Array Into Equal Pairs
#

# @lc code=start
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        seen = set()

        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                seen.remove(num)
        
        return len(seen) == 0# @lc code=end

