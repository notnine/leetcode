class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # e.g. text1: abcdef & text2: ge
        #   a b c d e f
        # g 0 0 0 0 0 0
        # e 0 0 0 0 1

        # e.g. text1: abcdef & text2: bcd
        #   a b c d e f
        # b 0 1
        # e     1 1 2
        # f           3

        n = len(text1)
        m = len(text2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        # recursion relation:
        # if curr letter match, dp[i][j] = 1 + dp[i-1][j-1]
        # else dp[i][j] = dp[i][j-1]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text2[i-1] == text1[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[m][n]

        # O(mn) time & space