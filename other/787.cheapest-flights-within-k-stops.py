#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#

# @lc code=start
from collections import deque, defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        # create adj. graph from flights
        adj = defaultdict(list) # adj[from] = (to, price)
        for from_i, to_i, price_i in flights:
            adj[from_i].append((to_i, price_i))
        
        # approach 0: bfs, keep track of price so far
        res = float('inf')
        my_d = deque([(src, 0)]) # queue tuples of (curr node, price so far)
        trips = -1

        while len(my_d) > 0:
            trips += 1

            for i in range(len(my_d)):
                node, price_so_far = my_d.popleft()
                if node == dst:
                    res = min(res, price_so_far)
                    continue
                for to_i, price_i in adj[node]:
                    my_d.append((to_i, price_so_far + price_i))
            
            if trips == k+1:
                return res
            
        return res if res != float('inf') else -1  
# @lc code=end

