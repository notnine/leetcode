#
# @lc app=leetcode id=1335 lang=python3
#
# [1335] Minimum Difficulty of a Job Schedule
#

# @lc code=start
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        
        memo = {} # memo[(i,days_left)] = min cost to schedule jobs 0..i with days_left days left

        def dfs(i: int, days_left: int) -> int:
            if (i, days_left) in memo:
                return memo[(i, days_left)]

            jobs_left = i + 1
            if days_left > jobs_left:
                return float('inf')
            
            if days_left == 1:
                return max(jobDifficulty[:i+1])
            
            best = float('inf')
            hardest = 0

            # there will be days_left - 1 after this, so we need at leasyt 1 job per days_left - 1
            for j in range(i, days_left - 2, -1):
                hardest = max(hardest, jobDifficulty[j])
                best = min(
                    best,
                    dfs(j - 1, days_left - 1) + hardest
                )
            
            memo[(i, days_left)] = best
            return best

        return dfs(n - 1, d)
# @lc code=end

