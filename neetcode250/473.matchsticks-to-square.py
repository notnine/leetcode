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

        memo = {}

        # return true if we can use all the matchsticks to make 1 square, where left, top, right, bottom represent the totals at each side so far
        def dfs(left: int, top: int, right: int, bottom: int, i: int) -> bool:
            if (left, top, right, bottom, i) in memo:
                return memo[(left, top, right, bottom, i)]

            # if we've used up all the matchsticks
            if i == len(matchsticks):
                if left == target and top == target and right == target and bottom == target:
                    return True
                else:
                    return False
            
            # if 1 side has too much
            if left > target or top > target or right > target or bottom > target:
                return False

            # try putting this matchstick in all sides
            put_left = dfs(left + matchsticks[i], top, right, bottom, i + 1) if left + matchsticks[i] <= target else False
            put_top = dfs(left, top + matchsticks[i], right, bottom, i + 1) if top + matchsticks[i] <= target else False
            put_right = dfs(left, top, right + matchsticks[i], bottom, i + 1) if right + matchsticks[i] <= target else False
            put_bottom = dfs(left, top, right, bottom + matchsticks[i], i + 1) if bottom + matchsticks[i] <= target else False
            memo[(left, top, right, bottom, i)] = put_left or put_top or put_right or put_bottom
            return memo[(left, top, right, bottom, i)]
            

        return dfs(0, 0, 0, 0, 0)
        
        
# @lc code=end

