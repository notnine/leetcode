#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)

        # while interval ends before newInterval begins, keep adding interval
        while i < n and newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
            i += 1
        
        # while interval conflicts with newInterval
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            i += 1
        res.append(newInterval)

        while i < n:
            res.append(intervals[i])
            i += 1

        return res

# @lc code=end
