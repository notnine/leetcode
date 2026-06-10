#
# @lc app=leetcode id=879 lang=python3
#
# [879] Profitable Schemes
#

# @lc code=start
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        memo = {}
        
        # given current index, members used, profit_so_far, return num of schemes that can be chosen
        def dfs(i: int, members_used: int, profit_so_far: int) -> int:
            if (i, members_used, profit_so_far) in memo:
                return memo[(i, members_used, profit_so_far)]
            
            if i == len(profit):
                return 1 if profit_so_far >= minProfit else 0
            
            members_left = n - members_used
            # to take
            to_take = 0
            if members_left >= group[i]:
                to_take = dfs(i + 1, members_used + group[i], min(profit_so_far + profit[i], minProfit))
            
            # to skip
            to_skip = dfs(i + 1, members_used, profit_so_far)

            memo[(i, members_used, profit_so_far)] = to_take + to_skip
            return memo[(i, members_used, profit_so_far)]
        
        return dfs(0, 0, 0) % (10**9+7)
# @lc code=end

