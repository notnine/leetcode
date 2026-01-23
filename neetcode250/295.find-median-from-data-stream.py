#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
class MedianFinder:

    def __init__(self):
        """
        Invariant 1: all elements in max_heap are less than or euqual to all elements in min_heap
        Invariant 2: abs(len(max_heap) - len(min_heap)) <= 1
        """
        self.max_heap = [] # max heap for lower half
        self.min_heap = [] # min heap for upper half

    def addNum(self, num: int) -> None:
        # get max of lower half
        max_lower_half = -self.max_heap[0] if self.max_heap else float('-inf')
        
        # place num into appropriate heap
        if num <= max_lower_half:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        
        # rebalance to guarantee invariant 2
        if abs(len(self.max_heap) - len(self.min_heap)) > 1:
            # if lower half has more elements
            if len(self.max_heap) > len(self.min_heap):
                moved = -heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, moved)
            else:
                moved = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -moved)

    def findMedian(self) -> float:
        n = len(self.max_heap) + len(self.min_heap)

        if n % 2 == 0:
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        
        if len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        else:
            return float(self.min_heap[0])
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

