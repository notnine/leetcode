#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#

# @lc code=start
class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        # approach 2: dp[(l,r)] = max([dp[(l,k)] + dp[(k,r)] + nums[l] * nums[k] * nums[r]] for k in range(l+1, r))

        # dp[(l, r)] is the max coins from popping all balloons between l and r exclusive.
        # for each k in (l, r) as the last balloon to pop, first pop left and right sides optimally, then pop k for nums[l] * nums[k] * nums[r].

        nums = [1] + nums + [1]
        n = len(nums)
        dp = dict()

        def dfs(l: int, r: int) -> int:
            if (l, r) in dp:
                return dp[(l, r)]

            if r - l <= 1:
                return 0

            best_so_far = 0

            for k in range(l+1, r):
                # find optimal left side
                optimal_left = dfs(l, k)                
                
                # find optimal right side
                optimal_right = dfs(k, r)

                curr_k = optimal_left + optimal_right + nums[l] * nums[k] * nums[r]
                best_so_far = max(best_so_far, curr_k)
            
            dp[(l, r)] = best_so_far
            return best_so_far


        return dfs(0, n-1) # remember (l, r) are exclusive in the recursion relation

        # run time analysis
        # num of distinct subproblems: possible num of l, r pairs are n^2
        # big o of each subproblem: possible num of k is r - l
        # so it is (n^2) * (n) all in all, O(n^3)
# @lc code=end

