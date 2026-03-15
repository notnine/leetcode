#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#

# @lc code=start
from collections import deque, defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        # approach 1: bellman ford with k relaxations
        cost = [float('inf')] * n # cost to get to i
        cost[src] = 0

        for _ in range(k+1):
            cost_copied = cost.copy() # deep copy to avoid "2 trips" in 1 round

            for from_i, to_i, price_i in flights:
                # see if we can get a cheaper flight to to_i
                cost_to_i = cost[from_i] + price_i
                cost_copied[to_i] = min(cost_to_i, cost_copied[to_i])
            
            cost = cost_copied
        
        return cost[dst] if cost[dst] != float('inf') else -1 
# @lc code=end

