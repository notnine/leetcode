#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        len_s, len_t = len(s), len(t)

        # given the ptr to s (i) and ptr to t (j) we are at, return num of distinct subsequences
        def dp(i: int, j: int) -> int:
            if (i, j) in memo:
                return memo[(i, j)]

            # found a sol
            if j == len_t:
                memo[(i, j)] = 1
                return 1
            
            # if the remainder of s is shorter than the remainder of t, we do not have enough chars
            if len_s - i < len_t - j or i >= len_s:
                memo[(i, j)] = 0
                return 0
            
            # if the curr char at s is not equal to curr char at t, increment i
            if s[i] != t[j]:
                memo[(i, j)] = dp(i + 1, j)
                return memo[(i, j)]
            
            # if the curr char at s is equal to curr char at t, we can either choose that char or skip it
            take = dp(i + 1, j + 1)
            skip = dp(i + 1, j)
            memo[(i, j)] = take + skip
            return memo[(i, j)]
        
        return dp(0, 0)
# @lc code=end

