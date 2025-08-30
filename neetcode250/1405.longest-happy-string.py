#
# @lc app=leetcode id=1405 lang=python3
#
# [1405] Longest Happy String
#

# @lc code=start
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        heap = []
        if a > 0:
            heap.append((-a, 'a'))
        if b > 0:
            heap.append((-b, 'b'))
        if c > 0:
            heap.append((-c, 'c'))
        
        heapq.heapify(heap)

        res = ''

        while heap:
            print(heap)
            print(res)
            print()

            f, c = heapq.heappop(heap)

            # if c is the same as the previous added character
            if res and res[-1] == c:
                # if no other option, not possible
                if not heap:
                    return res
                # add the second most frequent character
                f2, c2 = heapq.heappop(heap)
                res += c2
                # re-add the original most frequent character (c), and 2nd most frequent character (c2)
                if f < 0:
                    heapq.heappush(heap, (f, c))
                if f2 + 1 < 0:
                    heapq.heappush(heap, (f2 + 1, c2))

            # if c is not the same as the previous added character
            else:
                amount = min(2, -f)
                for _ in range(amount):
                    res += c
                if f + amount < 0:
                    heapq.heappush(heap, (f + amount, c))

        return res


                            

# @lc code=end

