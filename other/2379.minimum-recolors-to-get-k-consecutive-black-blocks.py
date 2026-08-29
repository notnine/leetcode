#
# @lc app=leetcode id=2379 lang=python3
#
# [2379] Minimum Recolors to Get K Consecutive Black Blocks
#

# @lc code=start
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        w = 0
        res = n + 1

        for i in range(n):
            if blocks[i] == 'W':
                w += 1
            
            if i >= k - 1:
                res = min(res, w)
                if blocks[i - k + 1] == 'W':
                    w -= 1
            
        return res
# @lc code=end

