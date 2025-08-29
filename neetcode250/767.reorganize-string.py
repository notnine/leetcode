#
# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#

# @lc code=start
#
# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#

# @lc code=start
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        s_ctr = Counter(s)
        heap = []
        for char in s_ctr:
            heap.append((-s_ctr[char], char))
        heapq.heapify(heap) # O (log n)

        # if most frequent frequency is > (n / 2) then not possible
        print(len(s) / 2)
        if -heap[0][0] > (len(s) + 1)/ 2:
            return ''

        res = ''

        # a: 2, b: 2
        # res = 'a'

        while heap:
            print(heap)
            # check if last element in res is the curr most element
            if res and res[-1] == heap[0][1]:
            # if it is: use second most element
                most_frequent_frequency, most_frequent_char = heapq.heappop(heap)
                f, c = heapq.heappop(heap)
                # re append the most frequent frequency, letter pair we are not using
                heapq.heappush(heap, (most_frequent_frequency, most_frequent_char))
                res += c
                if f < -1:
                    heapq.heappush(heap, (f + 1, c))

            # if it is NOT: use it
            else:
                f, c = heapq.heappop(heap)
                res += c
                if f < -1:
                    heapq.heappush(heap, (f + 1, c))
                
        return res
            

        
# @lc code=end


            

        
# @lc code=end

