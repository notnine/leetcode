#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 1 -> fresh orange, 2 -> rotten orange
        # if no oranges -> return 0
        # if impossible -> return -1

        # iterate thru grid, running bfs the first batch of rotten oranges as the first "level"
        # the num of mins is equiv. to the number of times our deque gets "refilled" (emptied & repopulated)
        # once we are can no longer infect any more oranges, run thru the grid one last time to check if there are still any fresh ones. return -1 if there are

        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        d = deque()
        mins = -1
        no_oranges = True
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 or grid[i][j] == 2:
                    no_oranges = False
                if grid[i][j] == 2:
                    d.append((i, j))
        
        if no_oranges:
            return 0

        while d:
            mins += 1
            # for each (i, j) in d, infect all of (i,j)'s neighbours
            for _ in range(len(d)):
                i, j = d.popleft()
                for d_i, d_j in dirs:
                    new_i, new_j = d_i + i, d_j + j
                    if 0 <= new_i < ROWS and 0 <= new_j < COLS and grid[new_i][new_j] == 1:
                        grid[new_i][new_j] = 2
                        d.append((new_i, new_j))

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return -1
        
        return mins
        
# @lc code=end

