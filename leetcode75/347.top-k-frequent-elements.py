#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_counter = Counter(nums)
        min_heap = []

        for num in nums_counter:
            heapq.heappush(min_heap, (nums_counter[num], num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [num for (count, num) in min_heap]
# @lc code=end

