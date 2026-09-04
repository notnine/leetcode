#
# @lc app=leetcode id=2929 lang=python3
#
# [2929] Distribute Candies Among Children II
#

# @lc code=start
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # n candies among 3 children, where each child gets no more than limit candies
        res = 0 

        for c1 in range(limit+1):
            # c3 will get n - c1 - c2. Find valid ranges of c2 and c3 given c1.
            low = max(0, n - c1 - limit)
            high = min(limit, n - c1)

            if low <= high:
                res += high - low + 1
        
        return res
# @lc code=end

