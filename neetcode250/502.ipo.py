#
# @lc app=leetcode id=502 lang=python3
#
# [502] IPO
#

# @lc code=start
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # build list of (capital, profit) tuples, sort in ascending order by capital

        capital_profit = []
        for i in range(len(profits)):
            capital_profit.append((capital[i], profits[i]))
        capital_profit.sort()
        print(capital_profit)
        i = 0 # points to the first project that is yet to be added into our max heap
        loop = 0
        max_heap = []

        # do below k times
        while loop < k:
            # maintain max heap that contains projects we can afford (project's capital <= w)
            while i < len(capital_profit) and capital_profit[i][0] <= w:
                heapq.heappush(max_heap, -capital_profit[i][1])
                i += 1

            # greedily pop from max heap, incrementing our w with that project's profit
            if max_heap:
                profit = -heapq.heappop(max_heap)
            else:
                return w # return if we cannot afford anything
            w += profit

            loop += 1
        
        return w

# @lc code=end

