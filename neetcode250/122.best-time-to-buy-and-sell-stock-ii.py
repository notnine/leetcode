#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr = prices[0]
        profit = 0

        for p in prices:
            if p < curr: # 'trade' holding stock for p
                curr = p

            elif p > curr: # sell for (curr - p) profit & hold stock p
                profit += (p - curr)
                curr = p
            
            else:
                continue

        return profit

# @lc code=end

