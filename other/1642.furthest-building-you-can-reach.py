#
# @lc app=leetcode id=1642 lang=python3
#
# [1642] Furthest Building You Can Reach
#

# @lc code=start
import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        diffs = []
        i = 0

        # keep using ladders, once we're out, greedily swap the smallest diff so far for bricks
        while i < n:
            if i+1 < n and heights[i+1] <= heights[i]:
                i += 1
                continue
            
            if i == n - 1:
                return n-1
            
            diff = heights[i+1] - heights[i]
            heapq.heappush(diffs, diff)
            if len(diffs) > ladders:
                min_diff = heapq.heappop(diffs)
                bricks -= min_diff
                if bricks < 0:
                    return i

            print("i, bricks, ladders: " + str([i, bricks, ladders]))
            print()
            i += 1
        


    def furthestBuilding_approach0(self, heights: List[int], bricks: int, ladders: int) -> int:
        memo = {}
        n = len(heights)

        # dfs(i, b, l) from index i, with b bricks and l ladders, return furthest building reachable
        def dfs(i, b, l) -> int:
            if (i, b, l) in memo:
                return memo[(i, b, l)]

            if i == n - 1:
                return 0
            
            if heights[i+1] <= heights[i]:
                res = 1 + dfs(i + 1, b, l)  
                memo[(i, b, l)] = res
                return res

            diff = heights[i+1] - heights[i]
            use_bricks, use_ladder = 0, 0
            # use bricks if enough
            if b >= diff:
                use_bricks = 1 + dfs(i+1, b-diff, l)

            # use ladder if enogh
            if l > 0:
                use_ladder = 1 + dfs(i+1, b, l-1)
            
            res = max(use_bricks, use_ladder)
            memo[(i, b, l)] = res
            return res

        return dfs(0, bricks, ladders)

# @lc code=end

