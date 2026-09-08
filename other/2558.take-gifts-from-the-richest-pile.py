#
# @lc app=leetcode id=2558 lang=python3
#
# [2558] Take Gifts From the Richest Pile
#

# @lc code=start
import heapq
import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = []

        for gift in gifts:
            heapq.heappush(heap, -gift)
        
        for _ in range(k):
            largest = -(heapq.heappop(heap))
            largest = math.floor(math.sqrt(largest))
            heapq.heappush(heap, -largest)
        
        return sum(heap) * -1  
# @lc code=end

