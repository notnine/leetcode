#
# @lc app=leetcode id=1631 lang=python3
#
# [1631] Path With Minimum Effort
#

# @lc code=start
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        heap = [(0, 0, 0)] # cost, r, c. Our priority queue
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        ROWS, COLS = len(heights), len(heights[0])
        costs = [[float('inf')] * COLS for _ in range(ROWS)]

        while heap is not None and len(heap) > 0:
            
            cost, r, c = heapq.heappop(heap)
            if r == ROWS - 1 and c == COLS - 1:
                return cost
            
            # for each neighbour, relax. if found better cost to reach neighbour, update it and add it to heap
            for d_r, d_c in directions:
                n_r, n_c = r + d_r, c + d_c
                if 0 <= n_r < ROWS and 0 <= n_c < COLS:
                    nei_cost = abs(heights[n_r][n_c] - heights[r][c])
                    cost_to_nei = max(cost, nei_cost)

                    # if found cheaper cost to neighbour, update costs & queue neighbour
                    if cost_to_nei < costs[n_r][n_c]:
                        costs[n_r][n_c] = cost_to_nei
                        heapq.heappush(heap, (cost_to_nei, n_r, n_c))

        return 0  
# @lc code=end

