#
# @lc app=leetcode id=873 lang=python3
#
# [873] Length of Longest Fibonacci Subsequence
#

# @lc code=start
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        best = 0
        n = len(arr)
        memo = {}
        arr_set = set(arr)
        num_to_i = {num: i for i, num in enumerate(arr)}
        
        # return max number we can add to make fib seubsequence starting at i,j
        def dfs(i: int, j: int) -> int:
            if (i, j) in memo:
                return memo[(i, j)]

            if arr[i] + arr[j] in num_to_i:
                new_j = num_to_i[arr[i] + arr[j]]
                res = 1 + dfs(j, new_j)
                memo[(i, j)] = res
                return res
            
            return 0


        for i in range(n - 1):
            for j in range(i+1, n):
                best = max(best, 2 + dfs(i, j))
        
        return best if best > 2 else 0
# @lc code=end

