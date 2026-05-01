#
# @lc app=leetcode id=1014 lang=python3
#
# [1014] Best Sightseeing Pair
#

# @lc code=start
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        prev_biggest = values[0] - 1
        prev_biggest_2 = values[1]
        if prev_biggest < prev_biggest_2:
            prev_biggest, prev_biggest_2 = prev_biggest_2, prev_biggest
        res = prev_biggest + prev_biggest_2

        # for i in range(n):
        #     for j in range(i+1, n):
        #         curr = values[i] + values[j] + i - j
        #         res = max(res, curr)

        for i in range(2, n):
            prev_biggest, prev_biggest_2 = prev_biggest - 1, prev_biggest_2 - 1
            curr_val = values[i]
            res = max(res, prev_biggest + curr_val, prev_biggest_2 + curr_val)
            if curr_val > prev_biggest:
                prev_biggest_2 = prev_biggest
                prev_biggest = curr_val
            if curr_val < prev_biggest and curr_val > prev_biggest_2:
                prev_biggest_2 = curr_val

        return res
# @lc code=end

