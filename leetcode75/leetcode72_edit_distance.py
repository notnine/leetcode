class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        
        # recursion relation:
        # dp[i][j] = min num of ops to transform first i letters of word1 to first j letters of word2
        # dp[i][j] = 
            # if curr chars equal, dp[i-1][j-1]
            # else 1 + min(insert, delete, replace)
        # Insert: pretend you inserted a character into word1 dp[i][j-1] + 1
        # Delete: pretend you deleted a character from word1 dp[i-1][j] + 1
        # Replace: pretend you replaced a character in word1 dp[i-1][j-1] + 1

        n = len(word1)
        m = len(word2)
        dp = [[float('inf') for _ in range(m + 1)] for _ in range(n + 1)]

        # init for when word1 & word2 are empty strings
        for i in range(n+1):
            dp[i][0] = i
        for j in range(m+1):
            dp[0][j] = j

        for i in range(1, n+1):
            for j in range(1, m+1):
                dp[i][j] = dp[i-1][j-1] if word1[i-1] == word2[j-1] else 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

        return dp[n][m]

        # O(nm) time & space