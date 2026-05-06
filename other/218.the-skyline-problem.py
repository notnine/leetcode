#
# @lc app=leetcode id=218 lang=python3
#
# [218] The Skyline Problem
#

# @lc code=start
import heapq
from collections import deque

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        events = []

        for l, r, h in buildings:
            events.append((l, -h, r))
            events.append((r, 0, 0))
        
        events.sort()

        res = []
        heap = [(0, float('inf'))]
        prev_h = 0

        for l, neg_h, r in events:
            if neg_h < 0:
                heapq.heappush(heap, (neg_h, r))

            while heap and heap[0][1] <= l:
                heapq.heappop(heap)
            
            curr_h = heap[0][0]

            if curr_h != prev_h:
                res.append([l, -curr_h])
                curr_h, prev_h = prev_h, curr_h
        
        return res
            

             
# @lc code=end

