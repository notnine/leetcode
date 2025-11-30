#
# @lc app=leetcode id=877 lang=python3
#
# [877] Stone Game
#

# @lc code=start
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}

        # return best score difference of current player
        def dp(l: int, r: int) -> int:
            if (l, r) in memo:
                return memo[(l, r)]
            if l == r:
                return piles[l]
            
            memo[(l, r)] = max(
                piles[l] - dp(l + 1, r),
                piles[r] - dp(l, r - 1)
            )
            return memo[(l, r)]
        
        return True if dp(0, len(piles) - 1) > 0 else False
# @lc code=end

