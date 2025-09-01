#
# @lc app=leetcode id=1863 lang=python3
#
# [1863] Sum of All Subset XOR Totals
#

# @lc code=start
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        memo = {}
        
        # return the sum all XOR totals for every subset of nums[i:]
        def backtrack(i: int, running_xor: int) -> int:
            if (i, running_xor) in memo:
                return memo[(i, running_xor)]
            if i == len(nums):
                return running_xor
            
            take = backtrack(i + 1, running_xor ^ nums[i])
            skip = backtrack(i + 1, running_xor)
            memo[(i, running_xor)] = take + skip
            return take + skip

        return backtrack(0, 0)
# @lc code=end

