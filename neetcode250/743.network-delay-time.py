#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start
from collections import defaultdict, deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        costs = [float('inf')] * (n + 1)
        costs[k] = 0
        adj = defaultdict(list) # map node u to its negibours (cost, neighbour)

        for u, v, t in times:
            adj[u].append((t, v))

        pq = deque([(0, k)]) # prio queue as min heap

        while pq is not None and len(pq) > 0:
            cost, node = pq.popleft()

            for nei_cost, nei_node in adj[node]:
                if cost + nei_cost < costs[nei_node]:
                    costs[nei_node] = cost + nei_cost
                    pq.append((cost + nei_cost, nei_node))

        most_expensive_node = max(costs[1:])
        return most_expensive_node if most_expensive_node != float('inf') else -1
# @lc code=end

