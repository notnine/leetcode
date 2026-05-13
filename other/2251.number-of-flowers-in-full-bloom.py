#
# @lc app=leetcode id=2251 lang=python3
#
# [2251] Number of Flowers in Full Bloom
#

# @lc code=start
import heapq
from collections import deque

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        # maintain a heap that contains the flowers currently in full bloom
        # at the arrival time of each person, to the heap, lazily remove flowers no longer in full bloom
        # and add flowers that are now in full bloom

        people_sorted = sorted(people)
        flowers.sort()
        i = 0 # pointer to which flower in flowers we are curr. at
        heap = [] # keeps track of the end times of the flowers currently in bloom
        p_to_flowers = {}

        for p in people_sorted:

            # remove flowers no longer in full bloom
            while heap and heap[0] < p:
                heapq.heappop(heap)

            # add flowers that are now in full bloom
            while i < len(flowers) and flowers[i][0] <= p:
                if p <= flowers[i][1]:
                    heapq.heappush(heap, flowers[i][1])
                i += 1

            p_to_flowers[p] = len(heap)

        res = []
        for p in people:
            res.append(p_to_flowers[p])

        return res
# @lc code=end

