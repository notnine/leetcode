class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1

        # recursion relation: dp[i][j] = num of unique paths to i,j, where i,j are the coords
        dp = []
        for row in range(m):
            dp.append([])
        for row in range(m):
            for col in range(n):
                if row == 0: dp[row].append(1) # there's only 1 way to travel to the coords in row 0
                elif col == 0: dp[row].append(1) # there's only 1 way to travel to the coords in col 0
                else: dp[row].append(0) # initialize every other coord

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]

        # O(mn) time & space