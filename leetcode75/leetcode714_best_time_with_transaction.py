from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        # dp[i][0] holds the local maximum profit when you do NOT have a stock in hand after day i.
        # dp[i][1] holds the local maximum profit when you ARE holding a stock after day i.
        dp = [[0] * 2 for _ in range(n)]
        
        dp[0][0] = 0            # No stock in hand initially
        dp[0][1] = -prices[0]   # Bought stock initially (so we spent money)

        for i in range(1, n):
            # If we are not holding a stock today: then either we did not have a stock yesterday, or we sold today
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)
            
            # If we are holding a stock today: then either we we were holding yesterday, or we bought today
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            
        return dp[n-1][0]  # max of holding

        # O(n) space & time