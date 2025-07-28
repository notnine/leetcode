#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        # i is our curr index
        def backtrack(i: int, comb: List[int]) -> None:
            if len(comb) == k:
                res.append(comb.copy())
                return
            
            for j in range(i+1, n+1):
                comb.append(j)
                backtrack(j, comb)
                comb.pop()


        backtrack(0, [])
        return res


# @lc code=end

