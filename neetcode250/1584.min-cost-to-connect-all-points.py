#
# @lc app=leetcode id=1584 lang=python3
#
# [1584] Min Cost to Connect All Points
#

# @lc code=start
from collections import deque

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def get_dist(point_a, point_b) -> int:
            """
            Return manhattan dist. b/w point_a & point_b
            """
            x_i, y_i = point_a
            x_j, y_j = point_b
            return abs(x_i - x_j) + abs(y_i - y_j)

        # thought process 1.0
        # queue every point to a priority queue, where the priority is given to the points closer to starting point
        # use dijkstra on that prio queue

        # thought process 2.0
        # maintain for each unvisited node, the cheapest way to connect it to our connected set, a minimum spanning tree
        # the key insight to building a minimum spanning tree is as follows:
        # we need to connect all points. at a step, we'd have a connected set (connected as cheaply) and we'd have unvisited points
        # we have to ensure that each unvisited point is compared to the len(connected set) at most once.
        # we accomplish this by: when adding a point to the connect set, compare that new point to each univisted node, and keep track of whether we've found a cheaper way to connect to that unvisited node.

        visited = set() # our connected set, tracked via index
        n = len(points)
        cost = [float('inf')] * n
        cost[0] = 0
        i = 0

        while len(visited) < n:
            point_a = points[i]
            visited.add(i)
            # cost[i] = 0 # cost from point i to itself is free, do we even need to do this?
            next_cheapest = None # next node to add

            for j, point_b in enumerate(points):
                if j in visited:
                    continue
                
                # for each unvisited point, update its cost if it's cheaper for it to connect to point_a (the point we are just added to our connected set)
                cost[j] = min(cost[j], get_dist(point_a, point_b))

                if next_cheapest is None or cost[next_cheapest] > cost[j]:
                    next_cheapest = j
            
            i = next_cheapest
        
        return sum(cost)


# @lc code=end

