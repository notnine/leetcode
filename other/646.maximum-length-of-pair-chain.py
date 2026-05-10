#
# @lc app=leetcode id=646 lang=python3
#
# [646] Maximum Length of Pair Chain
#

# @lc code=start
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:x[1]) # sort by end
        curr_longest = 0
        curr_end = -float('inf')

        for pair in pairs:
            start, end = pair[0], pair[1]
            if start > curr_end:
                curr_longest += 1
                curr_end = end
        
        return curr_longest

    def findLongestChain_archive(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        pair_to_index = {} # map the tuple_pair to its index in pairs
        n = len(pairs)

        for i, pair in enumerate(pairs):
            tuple_pair = tuple(pair)
            pair_to_index[tuple_pair] = i

        memo = {}

        # dp: return longest chain starting with given pair
        def dfs(pair: List[int]) -> int:
            tuple_pair = tuple(pair)
            if tuple_pair in memo:
                return memo[tuple_pair]
            
            i = pair_to_index[tuple_pair]
            curr_best = 0
            for j in range(i + 1, n):
                if pairs[j][0] > pair[1]:
                    # we can form a link with pair at j
                    curr_best = max(curr_best, 1 + dfs(pairs[j]))
            
            memo[tuple_pair] = curr_best if curr_best > 0 else 1
            return memo[tuple_pair]


        res = 0
        for pair in pairs:
            res = max(res, dfs(pair))
        
        return res
# @lc code=end

