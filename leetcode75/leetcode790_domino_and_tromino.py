class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5
        
        dp = [0 for _ in range(n+1)]

        dp[1] = 1
        dp[2] = 2
        dp[3] = 5

        # dp[i] = number of ways to tile 2 x i
        # recursion relation: dp[i] = 2*dp[i-1] + dp[i-3]
        
        for i in range(4, n + 1):
            dp[i] = 2 * dp[i-1] + dp[i-3]
        return dp[n] % (10**9 + 7)

        # O(n) space & time