#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # brute force would be to have 3 loops, and then check whether the sum is 0. O(n^3)
        # this can be optimized by keeping the outer loop, and replacing the inner 2 loops with optimal 2sum. O(n^2)
        res = []
        res_seen = set()

        # [-1,0,1,2,-1,-4]
        for i, n1 in enumerate(nums):
            target = -n1
            seen = set()
            for j, n2 in enumerate(nums[i+1:]): # run 2sum
                if target - n2 in seen and set([n1, n2, target-n2]) not in res_seen:
                    res.append([n1, n2, target - n2])
                    res_seen.add(frozenset({n1, n2, target-n2}))
                seen.add(n2)
        
        return res
# @lc code=end

