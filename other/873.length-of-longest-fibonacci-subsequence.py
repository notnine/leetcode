#
# @lc app=leetcode id=873 lang=python3
#
# [873] Length of Longest Fibonacci Subsequence
#

# @lc code=start
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        best = 0
        arr_set = set(arr)
        n = len(arr)

        for i in range(n-1):
            for j in range(i+1, n):
                prev, curr = arr[i], arr[j]
                nxt = prev + curr
                l = 2

                while nxt in arr_set:
                    l += 1
                    prev, curr = curr, nxt
                    nxt = prev + curr
                    best = max(best, l)
        
        return best
# @lc code=end

