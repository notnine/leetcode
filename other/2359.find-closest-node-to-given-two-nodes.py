#
# @lc app=leetcode id=2359 lang=python3
#
# [2359] Find Closest Node to Given Two Nodes
#

# @lc code=start
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        
        # each node only has 1 outgoing path, so there's only 1 path to follow
        # for node1, node2, calculate the dist from them, to every other node
        # for every node, find the node s.t. min(max(dist from node1 to this node, dist from node2 to this node))

        dist1 = {}
        dist2 = {}
        dist1[node1] = 0
        dist2[node2] = 0

        # fidn the distances from node1 to every other node, put in dist1
        curr = node1
        nxt = edges[node1]
        dst = 0
        while nxt != curr and nxt != -1 and nxt not in dist1:
            dst += 1
            dist1[nxt] = dst
            curr = nxt
            nxt = edges[curr]

        # find dists from node2 to every other node, put in dist2
        curr = node2
        nxt = edges[node2]
        dst = 0
        while nxt != curr and nxt != -1 and nxt not in dist2:
            dst += 1
            dist2[nxt] = dst
            curr = nxt
            nxt = edges[curr]

        # iterate thru all nodes 0..n-1 return min(max(.. , ..))
        res = float('inf')
        index = -1
        for node in range(len(edges)):
            if node not in dist1 or node not in dist2:
                continue
            curr = max(dist1[node], dist2[node])
            if res > curr:
                res = curr
                index = node

        return index
# @lc code=end

