import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        total_cost = 0
        n = len(costs)
        l, r = 0, n - 1

        l_heap, r_heap = [], []

        # pre-fill both heaps
        for _ in range(candidates):
            if l <= r:
                heapq.heappush(l_heap, (costs[l], l)) # append as a tuple (cost, index) to break ties using index
                l += 1
            if l <= r:
                heapq.heappush(r_heap, (costs[r], r))
                r -= 1
        
        # hire k workers
        for _ in range(k):
            if not r_heap or (l_heap and l_heap[0] <= r_heap[0]):
                worker_cost, _ = heapq.heappop(l_heap)
                total_cost += worker_cost
                # pre-fill for next round
                if l <= r:
                    heapq.heappush(l_heap, (costs[l], l))
                    l += 1
            else:
                worker_cost, _ = heapq.heappop(r_heap)
                total_cost += worker_cost
                # pre-fill for next round
                if l <= r:
                    heapq.heappush(r_heap, (costs[r], r))
                    r -= 1
        
        return total_cost
    
    # time O(candidates log candidates + k log candidates)
    # space O(candidates)
    