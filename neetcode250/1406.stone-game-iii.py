#
# @lc app=leetcode id=1406 lang=python3
#
# [1406] Stone Game III
#

# @lc code=start
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        memo = {}

        def dp(i: int) -> int:
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            
            best = -float('inf')
            take = 0
            for k in range(3):
                if i + k < n:
                    take += stoneValue[i + k]
                    best = max(best, take - dp(i + k + 1))
            memo[i] = best
            return best
        
        res = dp(0)
        if res < 0:
            return 'Bob'
        elif res > 0:
            return 'Alice'
        else:
            return 'Tie'
# @lc code=end

