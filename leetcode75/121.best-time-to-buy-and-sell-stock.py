#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        res = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[l] >= prices[r]:
                l = r
                r += 1
            else:
                diff = prices[r] - prices[l]
                res = max(res, diff)
                r += 1
        
        return res

# @lc code=end

