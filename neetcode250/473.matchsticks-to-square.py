#
# @lc app=leetcode id=473 lang=python3
#
# [473] Matchsticks to Square
#

# @lc code=start
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)

        if total % 4 != 0:
            return False
        
        target = total // 4

        curr = [0, 0, 0, 0] # left, top, right, bottom
        matchsticks.sort(reverse=True)
        memo = {}

        def dfs(i: int) -> bool:
            if i in memo:
                return memo[i]

            if i == len(matchsticks):
                return True

            # put matchsticks[i] at left side
            curr[0] += matchsticks[i]
            put_left = dfs(i+1) if curr[0] <= target else False
            curr[0] -= matchsticks[i]

            # put matchstick at top side
            curr[1] += matchsticks[i]
            put_top = dfs(i+1) if curr[1] <= target else False
            curr[1] -= matchsticks[i]

            # put matchstick at right side
            curr[2] += matchsticks[i]
            put_right = dfs(i+1) if curr[2] <= target else False
            curr[2] -= matchsticks[i]

            # put matchstick at bottom side
            curr[3] += matchsticks[i]
            put_bottom = dfs(i+1) if curr[3] <= target else False
            curr[3] -= matchsticks[i]

            memo[i] = put_left or put_top or put_right or put_bottom
            return put_left or put_top or put_right or put_bottom


        return dfs(0)

        
# @lc code=end

