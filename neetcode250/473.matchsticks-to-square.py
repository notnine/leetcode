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
        matchsticks.sort(reverse=True) # early pruning: put down big matchsticks first

        def backtrack(i: int) -> bool:
            if i == len(matchsticks) and curr[0] == curr[1] == curr[2] == curr[3] == target:
                return True

            # try putting matchstick in all sides
            for j in range(4):
                if curr[j] + matchsticks[i] <= target:
                    curr[j] += matchsticks[i]
                    if backtrack(i+1):
                        return True # early True return since we only need to find 1 sol
                    curr[j] -= matchsticks[i] # take matchstick back to try putting it in another side
                if curr[j] == 0: # if we just placed the matchstick into an empty side, don't need to try putting it in another side since they're all empty too (symmetrical)
                        break
            return False

        return backtrack(0)

        
# @lc code=end

