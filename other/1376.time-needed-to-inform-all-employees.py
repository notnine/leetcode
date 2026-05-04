#
# @lc app=leetcode id=1376 lang=python3
#
# [1376] Time Needed to Inform All Employees
#

# @lc code=start
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        # traverse to all leaves, calculating most expensive route

        subordinates = {i: [] for i in range(n)}

        for i in range(n):
            if manager[i] != -1:
                subordinates[manager[i]].append(i)

        # dfs, keep track of most expensive route
        # return most expensive route from employee i as root
        def dfs(i: int) -> int:
            if subordinates[i] == []:
                return 0
            res = 0
            for subordinate in subordinates[i]:
                res = max(res, dfs(subordinate) + informTime[i])
            return res
        
        return dfs(headID)
# @lc code=end

