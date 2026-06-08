#
# @lc app=leetcode id=2418 lang=python3
#
# [2418] Sort the People
#

# @lc code=start
import heapq
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        heap = []
        n = len(names)

        for i in range(n):
            heapq.heappush(heap, (-heights[i], names[i]))
        
        res = []
        while heap:
            height, name = heapq.heappop(heap)
            res.append(name)
        
        return res

        # O(n log n) time

# @lc code=end

